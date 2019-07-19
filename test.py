import MySQLdb
import os

host = '127.0.0.1'
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

<<<<<<< HEAD
<<<<<<< HEAD
prods = cur.execute("SELECT 'name','unitprice' FROM 'products' WHERE 'name' LIKE {}".format(search_string))
=======
<<<<<<< HEAD
prods = cur.execute("SELECT name,unitprice FROM products WHERE name LIKE \'{}\'".format(search_string) )
=======
prods = cur.execute("SELECT 'name','unitprice' FROM 'products' WHERE 'name' LIKE {}".format(search_string))
>>>>>>> 6038b51eaf6cfe6ea499bd618cd5a997a0ff9be0
>>>>>>> ca2fb1e1225af10f8ec332a33d9c37f6b26b65ed
=======
prods = cur.execute("SELECT 'name','unitprice' FROM 'products' WHERE 'name' LIKE {}".format(search_string))
>>>>>>> 30b76ce8478930ab187c69d5bed11b963ba4f168

print(prod)

for prod in cur:
    print(prod[0])
    print(prod[1])
