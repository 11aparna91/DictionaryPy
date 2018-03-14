import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root',password='123456',database='mysql',host='localhost')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
   cur = cnx.cursor()
   cur.execute( "SELECT words, meaning FROM dictionary" )
   for words, meaning in cur.fetchall() :
        print words, meaning
   cnx.close()
