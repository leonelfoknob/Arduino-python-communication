from mysql_connection import *
import mysql.connector
import serial
import time

ser = serial.Serial('COM4',9600, timeout=0.1)

conn = mysql.connector.connect(user='root', password='', host='localhost', database='data_pressure')
cursor = conn.cursor()
'''val = 12
#insert_data = """INSERT INTO data(data) VALUES (val)"""
query = f"INSERT INTO data (data) VALUES ('{val}')"

cursor.execute(query)
conn.commit()
#conn.close()
print("Data inserted")
print(cursor.rowcount, "record inserted.")'''

while True:
    data = ser.readline()
    if data:#verifi si la ligne n'est pas vide si c'est vide sa ne fait rien au cas contraire sa enregistre et sa break
        value = data.decode('utf-8')
        query = f"INSERT INTO data (data) VALUES ('{value}')"
        cursor.execute(query)
        conn.commit()
        print(value)
        print("Data inserted")
        time.sleep(1)
        '''try:# Executing the SQL command
        	cursor.execute(insert_data)
        	print(value)
        	print("Data inserted")
        	# Commit your changes in the database
        	conn.commit()
        except:# Rolling back in case of error
        	conn.rollback()
        time.sleep(1)
        conn.close()'''



'''
try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()
'''