import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'root', 'mydb');




sql_data = {
    "idPlayer": 1,
    "name": "Gold",
    "counter": 100,
}
sql_query = """UPDATE money SET counter=counter+%(counter)s WHERE idPlayer=%(idPlayer)s AND
               name=%(name)s"""

with con:
    cur = con.cursor()
    cur.execute(sql_query, sql_data)
    cur.execute("SELECT * FROM money")
    for row in cur.fetchall():
        print(row)
