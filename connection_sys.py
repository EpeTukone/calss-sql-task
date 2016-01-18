import MySQLdb
from _mysql import IntegrityError
ModelIntegrityError = IntegrityError
con = MySQLdb.connect('localhost', 'root', 'mysql', 'players')