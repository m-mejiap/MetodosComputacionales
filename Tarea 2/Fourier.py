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
timg11 = np.fft.fft2(img1)
timg1 = np.fft.fftshift(timg11)
timg22 = np.fft.fft2(img2)
timg2 = np.fft.fftshift(timg22)

#Grafica de los espectros de Fourier.
plt.figure(figsize=(10,10))

pl11 = plt.subplot(2,2,1)
pl11.imshow(np.abs(timg11),norm=LogNorm())
pl11.set_title("Espectro de Fourier para la imagen 1.")

pl21 = plt.subplot(2,2,2)
pl21.imshow(np.abs(timg22),norm=LogNorm())
pl21.set_title("Espectro de Fourier para la imagen 2.")

pl1 = plt.subplot(2,2,3)
pl1.imshow(np.abs(timg1),norm=LogNorm())
pl1.set_title("Espectro 1 de Fourier con np.shift.")

pl2 = plt.subplot(2,2,4)
pl2.imshow(np.abs(timg2),norm=LogNorm())
pl2.set_title("Espectro 2 de Fourier con np.shift.")

plt.savefig("FFtIm.pdf")

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

#Transformadas inversas de Fourier.
ahh1 = np.fft.ifftshift(ctimg1)
ehh1 = np.fft.ifft2(ahh1)
ahh2 = np.fft.ifftshift(ctimg2)
ehh2 = np.fft.ifft2(ahh2)

plt.figure(figsize=(10,10))
#Espectro filtrado de Fourier.
pl1 = plt.subplot(2,2,1)
pl1.imshow(np.abs(ctimg1),norm=LogNorm())
pl1.set_title("Espectro filtrado para la imagen 1.")

pl2 = plt.subplot(2,2,2)
pl2.imshow(np.abs(ctimg2),norm=LogNorm())
pl2.set_title("Espectro filtrado para la imagen 2.")

#Imagenes filtradas por separado.
pl11 = plt.subplot(2,2,3)
pl11.imshow(np.abs(ehh1), plt.cm.gray)
pl11.set_title("Resultado imagen 1 filtrada.")

pl21 = plt.subplot(2,2,4)
pl21.imshow(np.abs(ehh2), plt.cm.gray)
pl21.set_title("Resultado imagen 2 filtrada.")

plt.figtext(0,0,u"Teniendo en cuenta que el np.shift ubica las frecuencias bajas en el centro del espectro de Fourier, se realizó para la imagen 1 \nun filtro pasa altas el cual cambió a cero la amplitud de todas aquellas frecuencias ubicadas en el centro del espectro \nPor otro lado, se hizo el proceso inverso para la imagen 2, generando un filtro pasabajas al mentener únicamente el centro del espectro.")
plt.savefig("ImProceso.pdf")

#Imagen hibrida final.
final = ehh1 + ehh2

plt.figure(figsize=(7,7))
plt.imshow(np.abs(final), plt.cm.gray)
plt.title(u"Imagen híbrida final.")
plt.savefig("ImHybrid.pdf")