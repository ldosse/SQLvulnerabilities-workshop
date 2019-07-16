#Get the Flask app

#Example code that I will use to develop the functionality
import MySQLdb #This module is currently not included in reqs.txt

host = '192.168.99.100'
user = 'myuser'
password = 'secret'
port = 3306
db = 'test'

conn = MySQLdb.Connection(
    host=host,
    user=user,
    passwd=password,
    port=port,
    db=db
)



isAuthenticated = False
# Example of how to insert new values:
#conn.query("""INSERT INTO mytable VALUES ('foo3', 'bar2')""")
def authenticate(user, passwd,conn=conn):
	conn.query("""SELECT ?,? FROM ? WHERE ?=\'user\' AND ?=\'passwd\'""")
	conn.commit()

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



#Tablle that allows you to set prices of things (Should also have a message to display for hints)
#/admin



#/login