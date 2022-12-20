import numpy as np                                                                         # Importing numpy and plotting packages.
import matplotlib.pyplot as plt


q1, q2 = input("Enter the charges q1 and q2: ").split()                                    # Getting the charge configuration from the user, 
x1, y1 = input("Enter the coordinates of charge q1: ").split()                             # the charge values and its position.
x2, y2 = input("Enter the coordinates of charge q2: ").split()

q1 = float(q1)                                                                             # receiving the inputs as float values.
q2 = float(q2)
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

e0 = 8.854E-12                                                                             # defining constants for the Potential function.
k = 1/(4*np.pi*e0)

a = np.linspace(-50,50,101)                   
X, Y = np.meshgrid(a,a)                                                                    # developing a meshgrid for plotting potential in 2D space.
                                                                                            
V = (k*q1)/(np.sqrt((X-x1)**2 + (Y-y1)**2)) + (k*q2)/(np.sqrt((X-x2)**2 + (Y-y2)**2))      # Potential function.

plt.pcolormesh(X,Y,V)                                                                      # Plotting the Potential 2D scalar field.
plt.colorbar()                                                                             # scale of Potential in color.
plt.show()

conc1 = [[0]*1]*101                                                                        # While np.diff function is used the no of rows and columns in Vx and Vy respectively 
conc2 = [[0]*101]*1                                                                        # gets reduced by 1 due to the difference taken inthe function V. To compensate this,
                                                                                           # a column of zeroes and a row of zeroes are concatenated to Vx and Vy respectively. 
Vx = np.diff(V,axis = 1,prepend = conc1)
Vy = np.diff(V,axis = 0,prepend = conc2)

print(Vx.shape,Vy.shape)                                                                   # Checking the shapes of the 2D array to see if x,y and u,v of the 
print(X.shape,Y.shape)                                                                     # streamplot function are of same size.

plt.streamplot(X,Y,np.negative(Vx),np.negative(Vy))                                        # Plotting the Electric field. The negative comes from the 
plt.axis("scaled")                                                                         # physics formula of the electric field.
plt.show()



















