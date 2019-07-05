import numpy as np
import matplotlib.pylab as plt

data1 = np.genfromtxt("dats.dat",delimiter=",",skip_footer=202)
data2 = np.genfromtxt("dats.dat",delimiter=",",skip_header=201,skip_footer=1)

plt.figure(figsize=(8,6))
plt.plot(data1[:,0],data1[:,1],color="grey",label="Euler.")
plt.plot(data1[:,0],np.exp(-data1[:,0]),color="black",label="Teorica.")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica: Solución EDO.")
plt.legend()
plt.savefig("g_Euler.png")

plt.figure(figsize=(8,6))
plt.plot(data2[:,0],data2[:,1],color="grey",label="Runge Kutta.")
plt.plot(data2[:,0],np.exp(-data1[:,0]),color="black",label="Teorica.")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica: Solución EDO.")
plt.legend()
plt.savefig("g_Runge.png")

plt.figure(figsize=(8,6))
plt.plot(data1[:,0], np.abs(np.exp(-data1[:,0])-data1[:,1]), color="grey",label="Error con Euler.")
plt.xlabel("x")
plt.ylabel('$|y_{\mathrm{true}}-y_{\mathrm{LF}}|$')
plt.title("Gráfica: Error.")
plt.legend()
plt.savefig("g_Euler_error.png")

plt.figure(figsize=(8,6))
plt.plot(data2[:,0], np.abs(np.exp(-data2[:,0])-data2[:,1]), color="grey",label="Error con Runge Kutta.")
plt.xlabel("x")
plt.ylabel('$|y_{\mathrm{true}}-y_{\mathrm{LF}}|$')
plt.title("Gráfica: Error.")
plt.legend()
plt.savefig("g_Ruge_error.png")