import matplotlib.pyplot as plt         # Importing plotting function
import numpy as np                      # Importing numpy function for exponential and linespace function


def f(x):                               # Defining the Integrand function
    return np.exp(-x**2)

N = 3000                                # No. of steps
a = 0                                   # start of interval
b = 3                                   # end of interval
h = (b-a)/N                             # step size
S = []                          
s = 0.5*f(a) + 0.5*f(b)                 # declaring summation variable
S.append(f(a))                          # Array to store independent integrated values 

for k in range(1,N):                    # For loop that sums up the integral
    int = f(a + k*h)                    # creates an array of the integrated values
    S.append(int)
    s += f(a + k*h)

print(h*s)                              # Printing integration value

x = np.linspace(a,b,N)                  # x coordinate
y = np.exp(-x**2)                       # y coordinate

plt.plot(x,S)                           # plotting the integrated graph
plt.title('Intergrated Function')         
plt.xlabel('x')
plt.ylabel('E(x)')
plt.show()                              # show the plot
