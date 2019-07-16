import numpy as np
import matplotlib.pylab as plt
from matplotlib.colors import LogNorm

#Punto 2: Transformada de Fourier: Imagenes hibridas.
#2a. Almacene los datos de las imagenes cara_02_grisesMF.png y de cara_03_grisesMF.png.
img1 = plt.imread("cara_02_grisesMF.png")
img2 = plt.imread("cara_03_grisesMF.png")

plt.figure(figsize=(10,10))

pl1 = plt.subplot(1,2,1)
pl1.imshow(img1, plt.cm.gray)
pl1.set_title("Imagen original 1.")

pl2 = plt.subplot(1,2,2)
pl2.imshow(img2, plt.cm.gray)
pl2.set_title("Imagen original 2.")

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

ctimg1[110:150,70:100] = 0

ctimg2[0:120,0:columnas2] = 0
ctimg2[135:filas2,0:columnas2] = 0
ctimg2[100:150,0:75] = 0
ctimg2[100:150,95:columnas2] = 0

#Espectro filtrado de Fourier.
plt.figure(figsize=(10,10))

pl1 = plt.subplot(1,2,1)
pl1.imshow(np.abs(ctimg1),norm=LogNorm())
pl1.set_title("Gráfica: Filtro para la imagen 1.")

pl2 = plt.subplot(1,2,2)
pl2.imshow(np.abs(ctimg2),norm=LogNorm())
pl2.set_title("Gráfica: Filtro para la imagen 2.")

#Transformadas inversas de Fourier.
ahh1 = np.fft.ifftshift(ctimg1)
ehh1 = np.fft.ifft2(ctimg1)
ahh2 = np.fft.ifftshift(ctimg2)
ehh2 = np.fft.ifft2(ctimg2)

#Imagenes filtradas por separado.
plt.figure(figsize=(10,10))

pl1 = plt.subplot(1,2,1)
pl1.imshow(np.abs(ehh1), plt.cm.gray)
pl1.set_title("Resultado 1.")

pl2 = plt.subplot(1,2,2)
pl2.imshow(np.abs(ehh2), plt.cm.gray)
pl2.set_title("Resultado 2.")

#Imagen hibrida final.
final = ehh1 + ehh2

plt.figure(figsize=(7,7))
plt.imshow(np.abs(final), plt.cm.gray)