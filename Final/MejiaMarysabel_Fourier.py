import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft
import matplotlib
matplotlib.use('Agg')

n = 1280 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 320 ) #320 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)

# Tiene una serie de tiempo, donde los datos de tiempo estan almacenados en un arreglo t y los datos de amplitud en un arreglo amp.
#1) Usando los paquetes de scipy de la transformada de Fourier, haga un FILTRO de la senial que elimine las frecuencias mayores a 1000Hz en las senial original.
#2) Haga una grafica de la senial original y la senial filtarada y guardela SIN MOSTRARLA en filtro.pdf

# SU FILTRO
trans = np.fft.fft(amp)
freq = np.fft.fftfreq(n,dt)
for i in range(len(freq)):
    if(freq[i]>1000 or freq[i]<-1000):
        trans[i] = 0
new = np.fft.ifft(trans)

# SU GRAFICA
plt.figure()
plt.plot(t,amp,color="dodgerblue",label="Señal original.")
plt.plot(t,new, color="blue", label="Señal filtrada.")
plt.xlabel("Tiempo.")
plt.ylabel("Amplitud.")
plt.legend()
plt.savefig("filtro.pdf")
