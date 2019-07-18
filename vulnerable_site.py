	#Get the Flask app
from flask import Flask, request, render_template
import MySQLdb
import os

vuln_app = Flask(__name__)
def hash(wrd):
	return wrd

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
#conn.query("""INSERT INTO mytable VALUES ('foo3', 'bar2')""")
def authenticate(user, passwd,conn=conn):
	passwd = hash(passwd)
	cur.execute("SELECT username,password FROM users WHERE username=\'{}}\' AND password=\'{}}\'".format(user,passwd))
	res = cur.fetchone()

	result = {'ValidUser':False, 'ValidPassword':False}
	if somethingTODO:
		result['ValidUser'] = True
	if something_elseTODO:
		result['ValidPassword'] = True

	return result


conn.commit()

# # Example of how to fetch table data:
# conn.query("""SELECT * FROM mytable""")
# result = conn.store_result()
# for i in range(result.num_rows()):
#     print(result.fetch_row())






#---------------ROUTES----------------------

#Form that allows you to search and see prices of things
#/shop
@vuln_app.route('/',methods=['GET','POST'])
def shop():
	if request.method == 'GET':
		return render_template('search.html',productList=[])

	else:

		search_string = "\'%"+ request.form.get('search')+"%\'"

		cur.execute("SELECT name,unitprice FROM products WHERE name LIKE {};".format(search_string) )
		productList = list(cur)
		return render_template('search.html',productList=productList)



#Table that allows you to set prices of things (Should also have a message to display for hints)
#/admin



#/login
@vuln_app.route('/login',methods= ['GET','POST'])
def login():
	if request.method == 'POST':
		#TODO: Ensure username and password are not empty first
		username = request.form.get('username')
		password = request.form.get('password')
		if not username or not password:
			return render_template('login.html', message='Please enter both Username and password')
		res = authenticate(username,password)
		msg = ''
		if res['ValidUser']:
			msg+= 'Valid Username'
		else:
			msg+= 'Invalid Username'

		if res['ValidPassword']:
			msg+= ' and Valid Password'
		else:
			msg+= ' and Invalid Password'

		if not (res['ValidUser'] and res['ValidPassword']):
			return render_template('login.html', message=msg)

		return url_for(success)



	else:
		'''Show the login form (for a get request)'''
		return render_template('login.html', message='')

if __name__ == '__main__':
	vuln_app.run(debug = False, host='0.0.0.0')
