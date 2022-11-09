#read data from arduino python cod
import serial
import time

ser = serial.Serial('COM4',9600, timeout=0.1)


#arduino = serial.Serial('COM3',115200, timeout=0.1)

def read_sensor_data():
    data = ser.readline()
    return data
    #return data.decode('utf-8')#convert reciving data by in string

while True:
    #value = read_sensor_data
    data = ser.readline()
    if data:#verifi si la ligne n'est pas vide si c'est vide sa ne fait rien au cas contraire sa enregistre et sa break
        value = data.decode('utf-8')
        print(value)