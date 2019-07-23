import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = np.genfromtxt("Canal_ionico.txt")

def circle(r):
    x = np.linspace(-r,r,100)
    return (np.sqrt(r**2-x**2))

def metodo(r_old0):
    r_old = r_old0
    r_new = np.random.normal(r_old,1,1)
    guarda = []
    alpha = r_old / r_new
    if (alpha<1):
        guarda.append(r_new)
        
plt.figure()
fig, ax = plt.subplots()
plt.axis('equal')
circle1 = plt.Circle((5, 5), np.max(5), color='r',fill=False)
ax.add_artist(circle1)
plt.savefig("Canal.png")
plt.scatter(data[:,0],data[:,1])
