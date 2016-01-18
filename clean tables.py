import MySQLdb
from connection_sys import con
r = ''
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM player")
    for row in cur.fetchall():
        r += str(row)
print r
sql_query = 'delete FROM players.player where id_player = %(id)s'
sql_data = {'id': r[1]}
with con:
    cur = con.cursor()
    cur.execute(sql_query, sql_data)