#Importing the packages
import numpy as np
import numpy.random as rnd


N = 10000000
z = rnd.random(N)
#Transformation formula
x = z**2

def g(x):
	return 1/(1+np.exp(x))

I = sum(g(x))/N*2

print('The evaluation of the Integral is: ',I)