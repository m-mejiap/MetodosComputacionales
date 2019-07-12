import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d

T_inicial = np.genfromtxt("data.dat")
T_2 = np.genfromtxt("data1.dat")
x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
x1,y1 = np.meshgrid(x,y)

fig = plt.figure(figsize=(15,7))

g = fig.add_subplot(1,2,1,projection='3d')
g.plot_surface(x1,y1,T_inicial,color="orange")
g.set_zlabel("Temperatura. (ºC)")
g.set_xlabel("Eje x. (m)")
g.set_ylabel("Eje y. (m)")
g.set_title("Gráfica: Condiciones iniciales.")

b = fig.add_subplot(1,2,2,projection='3d')
b.plot_surface(x1,y1,T_2,color="blue")
b.set_zlabel("Temperatura. (ºC)")
b.set_xlabel("Eje x. (m)")
b.set_ylabel("Eje y. (m)")
b.set_title("Gráfica: Segundas Condiciones iniciales.")

plt.savefig("plots_difusion.png")