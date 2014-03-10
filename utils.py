# utils.py 
import MySQLdb 

#DATABASE='estateFinderDB' 
#DB_USER = 'estate' 
#DB_PASSWORD = 'blogPassword' 
#HOST = 'localhost' 

def db_connect(): 
   return MySQLdb.connect('localhost', 'estate', '', 'estateFinderDB')