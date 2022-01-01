#this cod send character command to arduino and control it.
# to use it download also *----arduino_receice_python_command.ino----* file to control your arduino with keybord keys
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

while True:
    num = input("Enter a number: ") # Taking input from user
    if num == '0' :#if your input is 0
        arduino.write(bytes(num, 'utf-8')) #by serial port send 0 charactere to arduino
        print("red_led on")
    elif num == '1':# if your input is 1
        arduino.write(bytes(num, 'utf-8')) #by serial port send 1 charactere to arduino
        print("green_led on...")
    
    value = num
    print(value) # printing the value
