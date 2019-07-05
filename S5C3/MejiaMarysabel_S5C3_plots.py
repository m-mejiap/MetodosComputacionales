import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat",delimiter=",",skip_footer=1)

plt.figure(figsize=(8,6))
plt.plot(data[:,0],data[:,1],color="grey",label="Resorte.")
plt.xlabel("Tiempo.")
plt.ylabel("Posición.")
plt.title("Gráfica: Posición en función del tiempo.")
plt.legend()
plt.savefig("MejiaMarysabelResorte.pdf")