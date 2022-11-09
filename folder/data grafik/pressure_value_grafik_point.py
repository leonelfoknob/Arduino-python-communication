#read data from arduino python cod
import serial
import time
import matplotlib.pyplot as plt

plt.ion()
fig=plt.figure()

i=0
x=list()
y=list()
i=0

ser = serial.Serial('COM4',9600, timeout=0.1)
ser.close()
ser.open()

while True:
    #value = read_sensor_data
    data = ser.readline()
    if data:#verifi si la ligne n'est pas vide si c'est vide sa ne fait rien au cas contraire sa enregistre et sa break
        #value = data.decode('utf-8')
        value = data.decode()
        x.append(i)
        y.append(value)
        plt.scatter(i, float(value))
        i += 1
        plt.show()
        plt.pause(0.0001)
        #print(value)