import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat",delimiter=",")

plt.figure(figsize=(7,5))
plt.plot(data[:,0],data[:,1],color="black",label="Orbita.")
plt.xlabel("Tiempo.")
plt.ylabel("Posición.")
plt.title(u"Gráfica: Posición en función del tiempo.")
plt.legend()