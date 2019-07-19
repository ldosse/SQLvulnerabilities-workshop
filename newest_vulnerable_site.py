# Get the Flask app
from flask import Flask, request, render_template
from hashlib import md5
from wtforms import Form, StringField
import MySQLdb
import os


class ShoppingForm(Form):
    search = StringField('search')


class LoginForm(Form):
    username = StringField('username')
    password = StringField('password')


vuln_app = Flask(__name__)


def hash(raw_passwrd):
    return md5(raw_passwrd.encode('utf-8')).hexdigest()


def check_hash(str_to_check, pw_hash):
    str_hash = hash(str_to_check)
    return (str_hash == pw_hash)


host = 'localhost'
user = os.environ['SQL_USER']
password = os.environ['SQL_PASS']
port = int(os.environ['SQL_PORT'])
db = os.environ['vuln_db']

conn = MySQLdb.Connect(
    host=host,
    user=user,
    passwd=password,
    port=port,
    db=db
)

cur = conn.cursor()

isAuthenticated = False


# Example of how to insert new values:
# conn.query("""INSERT INTO mytable VALUES ('foo3', 'bar2')""")
def authenticate(user, passwd, conn=conn):
    res = cur.execute("SELECT username,password FROM users WHERE username=\"{}\";".format(user))
    # res = cur.fetchone()
    res2 = list(cur)
    result = {'ValidUser': False, 'ValidPassword': False}
    if res:
        result['ValidUser'] = (res2[0][0] == user)
        result['ValidPassword'] = check_hash(password,res2[0][1])

    conn.commit()

    return result


# # Example of how to fetch table data:
# conn.query("""SELECT * FROM mytable""")
# result = conn.store_result()
# for i in range(result.num_rows()):
#     print(result.fetch_row())


# ---------------ROUTES----------------------

# Form that allows you to search and see prices of things
# /shop
@vuln_app.route('/', methods=['GET', 'POST'])
def shop():
    form = ShoppingForm(request.form)
    if request.method == 'GET':
        return render_template('search.html', productList=[], form=form)

    else:
        search_string = "\'%" + form.search.data + "%\'"
        cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string))
        productList = list(cur)
        cur.commit()
        return render_template('search.html', productList=productList, form=form)


# Table that allows you to set prices of things (Should also have a message to display for hints)
# /admin


# /login
@vuln_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        # TODO: Ensure username and password are not empty first
        username = form.username.data
        password = form.password.data
        if not username or not password:
            return render_template('login.html', message='Please enter both Username and password', form=form)
        result = authenticate(username, password)
        msg = ''
        if result['ValidUser']:
            msg += 'Valid Username'
        else:
            msg += 'Invalid Username'

        if result['ValidPassword']:
            msg += ' and Valid Password'
        else:
            msg += ' and Invalid Password'

        if not (result['ValidUser'] and result['ValidPassword']):
            return render_template('login.html', message=msg, form=form)

        return url_for(success)



    else:
        '''Show the login form (for a get request)'''
        return render_template('login.html', message='', form=form)


# /buy
@vuln_app.route('/buy', methods=['GET'])
def buy():
    return render_template('success.html')


if __name__ == '__main__':
    vuln_app.run(debug=False, host='0.0.0.0')
