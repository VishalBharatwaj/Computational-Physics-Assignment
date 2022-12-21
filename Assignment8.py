import numpy as np
import matplotlib.pyplot as plt

def trajectory(m = 1):
	
	def f(r,t):
		ro = 1.22
		C = 0.47
		g = 9.81
		R = 8e-2
		x,y,vx,vy = r
		v = np.sqrt(vx**2 + vy**2)
		F_fr = 1/2*np.pi*R**2*ro*C*v**2
		Dr = [vx,vy]
		Dvx = -F_fr/m*vx/v
		Dvy = -F_fr/m*vy/v - g
		Dv = [Dvx,Dvy]
		return Dr + Dv
		
	r0 = [0,0]
	v0e = 100*np.exp(1j*30/180*np.pi)
	v0 = [v0e.real,v0e.imag]
	initial_conditions = r0 + v0
	
	I0 = np.array(initial_conditions, float)
	a = 0
	b = 10
	N = 10
	h = (b-a)/N
	
	tpoints = np.arange(a,b,h)
	solution = np.empty(tpoints.shape + I0.shape, float)
	r = I0
	
	for i,t in enumerate(tpoints):
		solution[i]=r
		k1 = h*np.array(f(r,t))
		k2 = h*np.array(f(r+0.5*k1,t+0.5*h))
		k3 = h*np.array(f(r+0.5*k2,t+0.5*h))
		k4 = h*np.array(f(r+k3,t+h))
		r += (k1+2*k2+2*k3+k4)/6
		
	t = tpoints
	x = solution[:,0]
	y = solution[:,1]
	
	plt.plot(x[y>0], y[y>0], label = 'm')
	
	return x[abs(y)<0.2][-1]      

m_range = np.arange(0.5,5,0.05)
x_ground = [trajectory(m) for m in m_range]

plt.show()


plt.plot(m_range,x_ground)
plt.xlabel('m')
plt.ylabel('x')
plt.show()