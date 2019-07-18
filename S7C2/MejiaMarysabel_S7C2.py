import numpy as np
import matplotlib.pylab as plt

#Ejercicio 1. 
x0 = np.linspace(-4,4,1000)
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.title(u"Gráfica: Función incial.")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("func.png")

def caminata(numpasos,sigma,x_guess):
    x_viejo = x_guess
    x_almacena = [x_guess]
    for i in range(1,numpasos):
        x_nuevo = np.random.normal(x_viejo,sigma,1)[0]
        alpha = mifun(x_nuevo)/mifun(x_viejo)
        if(alpha>=1):
            x_almacena.append(x_nuevo)
        if(alpha<1):
            beta = np.random.random(1)[0]
            if(beta<alpha):
                x_almacena.append(x_nuevo)
            if(beta>alpha):
                x_almacena.append(x_viejo)
        x_viejo = x_nuevo
    return x_almacena

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(1000,0.1,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 4.")
plt.savefig("histograma_str(0.1)_str(1000).pdf")

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(100000,5,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 1.")
plt.savefig("histograma_str(5)_str(100000).pdf")

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(100000,0.2,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 2.")
plt.savefig("histograma_str(0.2)_str(100000).pdf")

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(100000,0.01,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 3.")
plt.savefig("histograma_str(0.01)_str(100000).pdf")

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(1000,0.1,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 4.")
plt.savefig("histograma_str(0.1)_str(1000).pdf")

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(100000,0.1,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 5.")
plt.savefig("histograma_str(0.1)_str(100000).pdf")

plt.figure()
plt.plot(x0,mifun(x0),color="black")
plt.hist(caminata(500000,0.1,-1.0), bins=100, density = True)
plt.title(u"Gráfica: Histograma 6.")
plt.savefig("histograma_str(0.1)_str(500000).pdf")