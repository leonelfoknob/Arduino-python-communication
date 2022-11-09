#static graf 
'''import matplotlib.pyplot as plt

# data
data_lst = [60, 59, 49, 51, 49, 52, 53]

# create the figure and axis objects
fig, ax = plt.subplots()

# plot the data and customize
ax.plot(data_lst)
ax.set_xlabel('Day Number')
ax.set_ylabel('Temperature (*F)')
ax.set_title('Temperature in Portland, OR over 7 days')

# save and show the plot
fig.savefig('static_plot.png')
plt.show()'''

#animated grafik
'''from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create empty lists for the x and y data
x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots()

def animate(i):
    pt = randint(1,9) # grab a random integer to be the next y-value in the animation
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])

ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)

plt.show()'''

import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i, data_lst, ser):  # ser is the serial object
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    flt = float(string)
    data_lst.append(flt)

    # Add x and y to lists
    data_lst.append(flt)
    # Limit the data list to 100 values
    data_lst = data_lst[-100:]
    # clear the last frame and draw the next frame
    ax.clear()
    ax.plot(data_lst)
    # Format plot
    ax.set_ylim([0,1050])
    ax.set_title('Potentiometer Reading Live Plot')
    ax.set_ylabel('Potentiometer Reading')

data_lst = []
fig, ax = plt.subplots()

ser = serial.Serial('COM4',9600, timeout=0.1)
time.sleep(2)
print(ser.name)
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(data_lst, ser), interval=200)
plt.show()

# after the window is closed, close the serial line
ser.close()
print("Serial line closed")