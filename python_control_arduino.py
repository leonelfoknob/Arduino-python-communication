import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

while True:
    num = input("Enter a number: ") # Taking input from user
    if num == '0' :
        arduino.write(bytes(num, 'utf-8'))
        print("red_led on")
    elif num == '1':
        arduino.write(bytes(num, 'utf-8'))
        print("green_led on...")
    
    value = num
    print(value) # printing the value