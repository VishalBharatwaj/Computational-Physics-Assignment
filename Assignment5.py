#Importing Required packages
import numpy as np
from numpy.fft import rfft,irfft
import matplotlib.pyplot as plt
import argparse 

#Defining discrete cosine transform
def dct(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]

    c = rfft(y2)
    phi = np.exp(-1j*np.pi*np.arange(N)/(2*N))
    return np.real(phi*c[:N])

#Defining discrete cosine transform
def idct(a):
    N = len(a)
    c = np.empty(N+1,complex)

    phi = np.exp(1j*np.pi*np.arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return irfft(c)[:N]

#Defining arguments to pass in the terminal
parser = argparse.ArgumentParser(description='Perform Fourier and Inverse Fourier transform on data in a text file')
parser.add_argument('index', type = str, help = 'text file 1 or text file 2')
args = parser.parse_args()
i = args.index

#Block of lines that run when the user input is 'dow'
if i=='dow':
	dow = open('dow.txt','r')
	data = dow.read().split('\n')
	
	c = rfft(data)
    
	n = np.arange(1,1025,1)
	
	c[103:]= 0
	data2 = irfft(c)
    
	c[21:] = 0
	data3 = irfft(c)
	
	plt.plot(n,data,label="Closing Value",color="blue")
	plt.plot(n,data2,label="Inverse Fourier 10%",color="red")
	plt.plot(n,data3,label="Inverse Fourier 2%",color="green")
	plt.legend()
	plt.show()

#Block of lines that run when the user input is 'dow2'
elif i=='dow2':
	dow2 = open('dow2.txt','r')
	data4 = dow2.read().split('\n')

	C = dct(data4)

	n = np.arange(1,1025,1)

	C[103:]= 0
	data5 = idct(C)

	C[21:] = 0
	data6 = idct(C)

	plt.plot(n,data4,label="Closing Value",color="blue")
	plt.plot(n,data5,label="Inverse Fourier 10%",color="red")
	plt.plot(n,data6,label="Inverse Fourier 2%",color="green")
	plt.legend()
	plt.show()

#Wrong argument checker
else:
	print("Wrong Argument")








	











