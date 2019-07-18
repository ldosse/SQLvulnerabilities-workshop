search_string = 'bag'
query = "SELECT name,unitprice FROM products WHERE name LIKE \'{}\';".format(search_string)
print (query)