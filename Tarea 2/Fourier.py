import numpy as np
import matplotlib.pylab as plt
from matplotlib.colors import LogNorm
from scipy.ndimage import gaussian_filter

#Punto 2: Transformada de Fourier: Imagenes hibridas.
#2a. Almacene los datos de las imagenes cara_02_grisesMF.png y de cara_03_grisesMF.png.
img1 = plt.imread("cara_02_grisesMF.png")
img2 = plt.imread("cara_03_grisesMF.png")

#2b. Haga los filtros de Fourier necesarios para realizar la imagen hibrida.
#Transformadas de Fourier.
timg1 = np.fft.fft2(img1)
timg1 = np.fft.fftshift(timg1)
timg2 = np.fft.fft2(img2)
timg2 = np.fft.fftshift(timg2)

#Grafica de los espectros de Fourier.
plt.figure(figsize=(10,10))

pl1 = plt.subplot(1,2,1)
pl1.imshow(np.abs(timg1),norm=LogNorm())
pl1.set_title("Gráfica: Espectro de Fourier para la imagen 1.")

pl2 = plt.subplot(1,2,2)
pl2.imshow(np.abs(timg2),norm=LogNorm())
pl2.set_title("Gráfica: Espectro de Fourier para la imagen 2.")

#Filtrado de imagenes.
ctimg1 = np.copy(timg1)
ctimg2 = np.copy(timg2)

filas1 = np.shape(ctimg1)[0]
columnas1 = np.shape(ctimg1)[1]
filas2 = np.shape(ctimg2)[0]
columnas2 = np.shape(ctimg2)[1]

ctimg1 = ctimg1 * (1 - gaussian_filter(np.abs(ctimg1),sigma=17))
ctimg2 = ctimg2 * gaussian_filter(np.abs(ctimg2),sigma=20)

plt.figure(figsize=(10,10))

pl1 = plt.subplot(1,2,1)
pl1.imshow(np.abs(ctimg1),norm=LogNorm())
pl1.set_title("Gráfica: Filtro para la imagen 1.")

pl2 = plt.subplot(1,2,2)
pl2.imshow(np.abs(ctimg2),norm=LogNorm())
pl2.set_title("Gráfica: Filtro para la imagen 2.")

#Imagen final.
ahh1 = np.fft.ifftshift(ctimg1)
ehh1 = np.fft.ifft2(ctimg1)
ahh2 = np.fft.ifftshift(ctimg2)
ehh2 = np.fft.ifft2(ctimg2)

plt.figure(figsize=(10,10))

pl1 = plt.subplot(1,2,1)
pl1.imshow(np.abs(ehh1), plt.cm.gray)
pl1.set_title("Resultado 1.")


pl2 = plt.subplot(1,2,2)
pl2.imshow(np.abs(ehh2), plt.cm.gray)
pl2.set_title("Resultado 2.")

final = ehh1 + ehh2

plt.figure()
plt.imshow(np.abs(final), plt.cm.gray)

Nota: 
Bajas frecuencias para lejos, altas frecuencias para cerca.
De cerca se ve a la persona seria y de lejos se ve a la persona sonriendo.
Cerca, seria, alta frecuencia, pasaaltas, imagen 1.
Lejos, sonriendo, baja frecuencia, pasabajas, imagen 2.