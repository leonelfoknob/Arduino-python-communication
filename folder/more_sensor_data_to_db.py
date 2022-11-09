from mysql_connection import *
import mysql.connector
import serial
import time

ser = serial.Serial('COM4',9600, timeout=0.1)

conn = mysql.connector.connect(user='root', password='', host='localhost', database='weater')
cursor = conn.cursor()


while True:
    data = ser.readline()
    if data:#verifi si la ligne n'est pas vide si c'est vide sa ne fait rien au cas contraire sa enregistre et sa break
        value = data.decode('utf-8')

        rows = [float(x) for x in value.split(',')]
        temperature = rows[0] 
        pressure = rows[1]
        altitude = rows[2]
        ReadSealevelPressure = rows[3]
        Real_altitude = rows[4]

        query = f"INSERT INTO weater_data (temperature,pressure,altitude,ReadSealevelPressure,Real_altitude) VALUES ('{temperature}','{pressure}','{altitude}','{ReadSealevelPressure}','{Real_altitude}')"
        cursor.execute(query)
        conn.commit()
        print("Data inserted")
        #time.sleep(1)
