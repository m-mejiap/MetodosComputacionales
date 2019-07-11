import numpy as np
import matplotlib.pylab as plt

data1 = np.genfromtxt("data.dat",delimiter=",",skip_footer=6007)
data2 = np.genfromtxt("data.dat",delimiter=",",skip_header=1001,skip_footer=5006)
data3 = np.genfromtxt("data.dat",delimiter=",",skip_header=2002,skip_footer=4005)
data4 = np.genfromtxt("data.dat",delimiter=",",skip_header=3003,skip_footer=3004)
data5 = np.genfromtxt("data.dat",delimiter=",",skip_header=4004,skip_footer=2003)
data6 = np.genfromtxt("data.dat",delimiter=",",skip_header=5005,skip_footer=1002)
data7 = np.genfromtxt("data.dat",delimiter=",",skip_header=6006,skip_footer=1)

plt.figure(figsize=(15,10))

pl1 = plt.subplot(2,2,1)
pl1.plot(data1[:,0],data1[:,1],color="black")
pl1.plot(data2[:,0],data2[:,1],color="grey")
pl1.plot(data3[:,0],data3[:,1],color="grey")
pl1.plot(data4[:,0],data4[:,1],color="grey")
pl1.plot(data5[:,0],data5[:,1],color="grey")
pl1.plot(data6[:,0],data6[:,1],color="grey")
pl1.plot(data7[:,0],data7[:,1],color="grey")
pl1.set_xlabel("x.")
pl1.set_ylabel("Amplitud.")
pl1.set_title("Gráfica: Amplitud en función de posición para cuerda con extremos fijos.")

plt.subplots_adjust(hspace=.3)
plt.savefig("plots.png")
