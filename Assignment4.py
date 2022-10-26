import numpy as np
import matplotlib.pyplot as plt


G=6.674e-11 
M=5.974e24 
m=7.348e22 
R=3.844e8 
w=2.662e-6 

def f(r):    
    return -w**2*r**5 + 2*w**2*R*r**4 - w**2*R**2*r**3 + G*r**2*(M-m) - 2*r*R*G*M +G*M*R**2 

def fprime(r):    
    return -5*w**2*r**4 + 8*w**2*R*r**3 - 3*w**2*R**2*r**2 + 2*G*r*(M-m) - 2*R*G*M 
    
r=np.linspace(0.1*R,0.99*R,100) 

plt.subplot(121) 
plt.plot(r,f(r), '-b') 
plt.grid() 
plt.subplot(122) 
plt.plot(r,fprime(r), '-b') 
plt.grid() 
plt.show()
eps=1e-4 
print('root      |error     |function val') 
error=10*eps 
x_1=3.2e8 

while error>eps:    
    x_2=x_1 - (f(x_1)/fprime(x_1))    
    error=np.abs(x_2-x_1)    
    x_1=x_2    
    print('{:.4e}|{:.4e}|{:.4e}'.format(x_2, error, f(x_2)))

