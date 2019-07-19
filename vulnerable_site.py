# Get the Flask app
from flask import Flask, request, render_template
from wtforms import Form, StringField
from hashlib import md5
import MySQLdb
import os


class ShoppingForm(Form):
    search = StringField('search')
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
    res = cur.execute("SELECT username,password FROM users WHERE username=\'{}\';".format(user))
    # res = cur.fetchone()
    result = {'ValidUser': False, 'ValidPassword': False}
    if res:
        result['ValidUser'] = (res[0][0] == user)
        result['ValidPassword'] = check_hash(res[0][1], password)

    conn.commit()

    return result


# # Example of how to fetch table data:
# conn.query("""SELECT * FROM mytable""")
# result = conn.store_result()
# for i in range(result.num_rows()):
#     print(result.fetch_row())


# ---------------ROUTES----------------------

<<<<<<< HEAD
<<<<<<< HEAD
# Form that allows you to search and see prices of things
# /shop
# @vuln_app.route('/', methods=['GET', 'POST'])
# def shop():
#     if request.method == 'GET':
#         cur.execute("SELECT name, unitprice FROM products;")
#         product_list = list(cur)
#         return render_template('search.html', productList=product_list)
#
#     else:
#
#         search_string = "\'"+request.form['search']+"\'"
#         cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string))
#         product_list = list(cur)
#         return render_template('search.html', productList=product_list)@vuln_app.route('/', methods=['GET', 'POST'])
@vuln_app.route('/', methods=['GET'])
def shop():
    if request.method == 'GET':
        search_string = "\'" + request.data['search'] + "\'" if (type(request.form.get('search')) == str) else "\'bag\'"
        cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string))
        product_list = list(cur)
        return render_template('search.html', productList=product_list)
=======
=======
>>>>>>> 30b76ce8478930ab187c69d5bed11b963ba4f168
#Form that allows you to search and see prices of things
#/shop
@vuln_app.route('/', methods=['GET', 'POST'])
def shop():
    form = ShoppingForm(request.form)
    if request.method == 'GET':
        return render_template('search.html', productList=[],form=form)

    else:
<<<<<<< HEAD
>>>>>>> ca2fb1e1225af10f8ec332a33d9c37f6b26b65ed

        search_string = "\'%"+request.form['search']+"%\'"
        cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string))
        product_list = list(cur)
        return render_template('search.html', productList=product_list)
# @vuln_app.route('/', methods=['GET'])
# def shop():
#     if request.method == 'GET':
#         search_string = "\'" + request.data['search'] + "\'" if (type(request.form.get('search')) == str) else "\'bag\'"
#         cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string))
#         product_list = list(cur)
#         return render_template('search.html', productList=product_list)

<<<<<<< HEAD
# Table that allows you to set prices of things (Should also have a message to display for hints)
# /admin

=======

# Table that allows you to set prices of things (Should also have a message to display for hints)
# /admin
>>>>>>> ca2fb1e1225af10f8ec332a33d9c37f6b26b65ed

# /login
@vuln_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # TODO: Ensure username and password are not empty first
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('login.html', message='Please enter both Username and password')
        result = authenticate(username, password)
        msg = ''
        if result['ValidUser']:
            msg += 'Valid Username'
        else:
            msg += 'Invalid Username'

<<<<<<< HEAD
        if result['ValidPassword']:
            msg += ' and Valid Password'
        else:
            msg += ' and Invalid Password'

=======
=======
        search_string = "\'%"+form.search.data+"%\'"
        # search_string = "\'%"+request.form['search']+"%\'"
        cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string))
        product_list = list(cur)
        return render_template('search.html', productList=product_list,form=form)


# Table that allows you to set prices of things (Should also have a message to display for hints)
# /admin


>>>>>>> 30b76ce8478930ab187c69d5bed11b963ba4f168
# /login
@vuln_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # TODO: Ensure username and password are not empty first
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('login.html', message='Please enter both Username and password')
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

<<<<<<< HEAD
>>>>>>> ca2fb1e1225af10f8ec332a33d9c37f6b26b65ed
=======
>>>>>>> 30b76ce8478930ab187c69d5bed11b963ba4f168
        if not (result['ValidUser'] and result['ValidPassword']):
            return render_template('login.html', message=msg)

        return url_for(success)



    else:
        '''Show the login form (for a get request)'''
        return render_template('login.html', message='')


# /buy
@vuln_app.route('/buy', methods=['GET'])
def buy():
    return render_template('success.html')


if __name__ == '__main__':
    vuln_app.run(debug=False, host='0.0.0.0')
