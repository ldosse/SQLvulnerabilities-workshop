#Get the Flask app
from flask import Flask
#Example code that I will use to develop the functionality
import sqlite3 #This module is currently not included in reqs.txt

vuln_app = Flask(__name__)


# host = '127.0.0.1'
# user = 'myuser'
# password = 'secret'
# port = 3306
db = 'vuln_shop.db'

# conn = sqlite3.Connect(
#     host=host,
#     user=user,
#     passwd=password,
#     port=port,
#     db=db
# )

conn = sqlite3.Connect(db)
cur = conn.cursor()



isAuthenticated = False
# Example of how to insert new values:
#conn.query("""INSERT INTO mytable VALUES ('foo3', 'bar2')""")
def authenticate(user, passwd,conn=conn):
	cur.execute("""SELECT ?,? FROM ? WHERE ?=\'user\' AND ?=\'passwd\'""")
	res = cur.fetchone()

	result = {'ValidUser':False, 'ValidPassword':False}
	if something:
		result['ValidUser'] = True
	if something_else:
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
@app.route('/',methods=['GET'],['POST'])
def shop():
	if request.method == 'GET':
		return render_template('search.html',productList=[])

	else:
		#TODO: Ensure username and password are not empty first


		cur.execute("""SELECT 'name','description','price' FROM ? WHERE 'name' LIKE *TODO*""" )




#Table that allows you to set prices of things (Should also have a message to display for hints)
#/admin



#/login
@app.route('/login',methods= ['GET','POST'])
def login():
	if request.method == 'POST':
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

