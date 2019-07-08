#Escriba un script en python llamado ApellidoNombre_S5C3_plots.py que Grafique con matplotlib dicha posición en función del tiempo y Guarde la gráfica obtenida en ApellidoNombreResorte.pdf

import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt("data.dat",delimiter=",",skip_footer=1,skip_header=1)

plt.figure(figsize=(8,6))
plt.plot(data[:,0],data[:,1],color="grey",label="Resorte.")
plt.xlabel("Tiempo.")
plt.ylabel("Posición.")
plt.title("Gráfica: Posición en función del tiempo.")
plt.legend()
plt.savefig("MejiaMarysabelResorte.pdf")
