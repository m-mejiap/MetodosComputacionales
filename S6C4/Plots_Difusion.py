import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d

T_inicial = np.genfromtxt("data.dat")
T_2 = np.genfromtxt("data1.dat")
T_3 = np.genfromtxt("data2.dat")
T_iniciall = np.genfromtxt("dataa.dat")
T_22 = np.genfromtxt("data11.dat")
T_33 = np.genfromtxt("data22.dat")
x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
x1,y1 = np.meshgrid(x,y)

fig = plt.figure(figsize=(15,10))

g = fig.add_subplot(3,3,1,projection='3d')
g.plot_surface(x1,y1,T_inicial,color="red")
g.set_zlabel("Temperatura. (ºC)")
g.set_xlabel("Eje x. (m)")
g.set_ylabel("Eje y. (m)")
g.set_title("Gráfica: Tiempo 0s.")

b = fig.add_subplot(3,3,2,projection='3d')
b.plot_surface(x1,y1,T_2,color="red")
b.set_zlabel("Temperatura. (ºC)")
b.set_xlabel("Eje x. (m)")
b.set_ylabel("Eje y. (m)")
b.set_title("Gráfica: Tiempo 100s.")

c = fig.add_subplot(3,3,3,projection='3d')
c.plot_surface(x1,y1,T_3,color="red")
c.set_zlabel("Temperatura. (ºC)")
c.set_xlabel("Eje x. (m)")
c.set_ylabel("Eje y. (m)")
c.set_title("Gráfica: Tiempo 2500s.")

gg = fig.add_subplot(3,3,4,projection='3d')
gg.plot_surface(x1,y1,T_iniciall,color="orange")
gg.set_zlabel("Temperatura. (ºC)")
gg.set_xlabel("Eje x. (m)")
gg.set_ylabel("Eje y. (m)")
gg.set_title("Gráfica: Tiempo 0s.")

bb = fig.add_subplot(3,3,5,projection='3d')
bb.plot_surface(x1,y1,T_22,color="orange")
bb.set_zlabel("Temperatura. (ºC)")
bb.set_xlabel("Eje x. (m)")
bb.set_ylabel("Eje y. (m)")
bb.set_title("Gráfica: Tiempo 100s.")

cc = fig.add_subplot(3,3,6,projection='3d')
cc.plot_surface(x1,y1,T_33,color="orange")
cc.set_zlabel("Temperatura. (ºC)")
cc.set_xlabel("Eje x. (m)")
cc.set_ylabel("Eje y. (m)")
cc.set_title("Gráfica: Tiempo 2500s.")

plt.savefig("plots_difusion.png")