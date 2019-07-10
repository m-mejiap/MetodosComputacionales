import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat",delimiter=",",skip_footer=1)

plt.figure(figsize=(8,6))
plt.scatter(data[:,0],data[:,1],color="grey",label="Cuerda.")
plt.xlabel("Tiempo.")
plt.ylabel("Amplitud.")
plt.title("Gráfica: Amplitud en función del tiempo.")
plt.legend()
plt.savefig("inicial.png")
