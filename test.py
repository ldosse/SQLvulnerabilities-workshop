import MySQLdb
import os

host ='127.0.0.1'
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

search_string = '%e%'

prods = cur.execute("SELECT name,unitprice FROM products WHERE name LIKE \'{}\';".format(search_string) )

print (prod)

for prod in cur:
	print(prod[0])
	print(prod[1])


