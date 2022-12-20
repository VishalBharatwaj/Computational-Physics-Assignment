#Initializing the packages
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint


L = 50
L0 = 48
#Number of iterations
motion_len = 1000
fig = plt.figure(figsize = (4,4))
ax = plt.axes(xlim = (-L, L), ylim = (-L, L))

X = int(input('If you want to check if the particle stays inside the box, type "48" else type "0": '))
#Defining the particle
particle = plt.Circle((X,0), radius = 1.5, facecolor = 'orange')
global x,y
x,y = X,0

#Defining the initial frame
def init():
    particle.center = (0, 0)
    ax.add_patch(particle)
    return particle,

#Animation function
def animate(j):
    global x,y
    particle.center = (x, y)
    #Generating random integers each defining one direction
    j = randint(1,4)
    #j = 1 refers to moving towards east
    if j == 1: 
        if x == L0:
            
            return particle,
        else:
            x += 1
            
            particle.center = (x, y)
            return particle,
    
    #j = 2 refers to moving towards west
    elif j == 2:
        if x == -L0:
            
            return particle,
        else:
            x -= 1
            
            particle.center = (x, y)
            return particle,

    #j = 3 refers to moving towards north        
    elif j == 3:
        if y == L0:
            
            return particle,
        else:
            y += 1
            
            particle.center = (x, y)
            return particle,

    #j = 4 refers to moving towards south        
    elif j == 4:
        if y == -L0:
            
            return particle,
        else:
            y -= 1
            
            particle.center = (x, y)
            return particle,
            
anim = animation.FuncAnimation(fig, animate, init_func = init,  frames = motion_len, interval = 20, blit = True)
plt.show()
#save as a gif
#writergif = animation.PillowWriter(fps=30)
#anim.save('Brownian.gif',writer=writergif)