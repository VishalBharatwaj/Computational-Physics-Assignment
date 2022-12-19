import matplotlib.pyplot as plt 
import numpy as np
from scipy.sparse import linalg 
from scipy import sparse as sparse
import matplotlib.animation as animation
 

def Quant_Tunnel(N, dt, width = 3.0, potential = 1.0, δ = 4.0, k = 1.5, x0 = -150.0, x_start = -200.0, x_end = 200.0):
    
    x, dx = np.linspace(x_start, x_end, N, retstep = True)        
 
    #Defining Gaussian Wave Function
    norm = (2.0 * np.pi * δ**2)**(-0.25)
    global Ψ
    Ψ = np.exp(-(x - x0)**2 / (4.0 * δ**2))
    Ψ = Ψ * np.exp(1.0j * (k) * x)
    Ψ = Ψ * norm
 
    #Potential Barrier
    V1 = np.array([potential if 0.0 < xx < width  else 0.0 for xx in x])
    #The following 2 lines can be uncommented to add another potential in the simulation.
    #All the instances of V1 should be replaced with V.
    #V2 = np.array([potential if 100.0 < xx < (100.0 + width)  else 0.0 for xx in x])
    #V = V1 + V2

    #Hamiltonian
    H_diag = (np.ones(N) / dx**2) + V1
    H_non_diag = np.ones(N - 1) * (-0.5 / dx**2)
    Hamiltonian = sparse.diags([H_diag, H_non_diag, H_non_diag], [0, 1, -1])
         
    #Evolution matrix
    Matrix1 = (sparse.eye(N) - dt / 2.0j * Hamiltonian).tocsc()
    Matrix2 = (sparse.eye(N) + dt / 2.0j * Hamiltonian).tocsc() 
    evolution_matrix = linalg.inv(Matrix1).dot(Matrix2).tocsr()
    
    #Function that calculates probability distribution for every dt.
    def evolve():
        global Ψ
        Ψ = evolution_matrix.dot(Ψ)
        prob = abs(Ψ)**2
        norm = sum(prob)
        prob /= norm
        Ψ /= norm**0.5
        return prob   
 
    #Plotting the graphs and setting the axes.
    fig, axis = plt.subplots()
    plt.plot(x, V1 * 0.1, color = 'r', label = 'Potential V(x)')
    Ψ_plot, = axis.plot(x, evolve(), color = 'g', label = 'Particle')
    axis.set_ylim(0, 0.1)
    axis.set_xlabel('Position (x)')
    axis.set_ylabel('Probability |Ψ|^2 ')
    global τ
    τ = 0.0
 
    #Function that updates the probability distribution data.
    def update(i):
        Ψ_plot.set_ydata(i)
        return Ψ_plot,
    
    #Function that calculates every frame.
    def time_step():
        global τ
        while (τ < 300):
            τ += dt
            yield evolve()
     
    
    anim = animation.FuncAnimation(fig, update, time_step, interval = 5)
    plt.legend()
    plt.show() 

print('Enter the required values for the simulation:\n')
N = int(input('Range of X-axis: '))
dt = float(input('Time step of wave equation: '))
width = float(input('Barrier width: '))
potential = float(input('Potential of the system: '))

#Ideal values N = 500, dt = 0.75, width = 15, potential = 0.9
Quant_Tunnel(N, dt, width, potential)