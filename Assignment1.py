#Importing the packages
import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0,2*np.pi,100)
#Deltoid Curve Equation
x = 2*np.cos(t) + np.cos(2*t)
y = 2*np.sin(t) - np.sin(2*t)
plt.grid()
plt.plot(x,y,label ='Deltoid curve')

t2 = np.linspace(0,10*np.pi,200)
r = t2**2
#Galilean Spiral
x2 = r*np.cos(t2)
y2 = r*np.sin(t2)
plt.plot(x2,y2,label='Galilean Spiral')

t3 = np.linspace(0,24*np.pi,1000)
#Fey's Function
R = np.exp(np.cos(t3)) - 2*np.cos(4*t3) + (np.sin(t3/12))**5
x3 = R*np.cos(t3)
y3 = R*np.sin(t3)
plt.plot(x3,y3,label="Fey's Function")


plt.legend()
plt.title('Parametric Graphs')
plt.xlabel('degrees')

plt.show()





