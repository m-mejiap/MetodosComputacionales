import numpy as np
import matplotlib.pylab as plt

data1 = np.genfromtxt("data.dat",delimiter=",",skip_footer=1002)
data2 = np.genfromtxt("data.dat",delimiter=",",skip_header=1001,skip_footer=1)

plt.figure(figsize=(15,10))

pl1 = plt.subplot(2,2,1)
pl1.plot(data1[:,0],data1[:,1],color="grey",label="Condición incial.")
pl1.set_xlabel("Tiempo.")
pl1.set_ylabel("Amplitud.")
pl1.set_title("Gráfica: Amplitud en función del tiempo.")
pl1.legend()

pl2 = plt.subplot(2,2,2)
pl2.plot(data2[:,0],data2[:,1],color="black",label="Cuerda paso 1.")
pl2.set_xlabel("Tiempo.")
pl2.set_ylabel("Amplitud.")
pl2.set_title("Gráfica: Amplitud en función del tiempo.")
pl2.legend()

plt.subplots_adjust(hspace=.3)
plt.savefig("plots.png")