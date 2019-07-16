import numpy as np
import matplotlib.pylab as plt

#Ejercicio 1.
#1a. Genere 1000 numeros aleatorios que sigan una distribucion uniforme y esten entre -10 y 10. Haga un histograma y guardelo sin mostrarlo en un archivo llamado uniforme.pdf.
numal = (20) * np.random.random(1000) - 10

plt.figure()
plt.hist(numal, bins=100)
plt.title(u"Gráfica: Histograma de números aleatorios uniformes.")
plt.savefig("uniforme.pdf")

#1b. Genere 1000 numeros aleatorios que sigan una distribucion gausiana centrada en 17 y de sigma 5. Haga un histograma y guardelo sin mostrarlo en un archivo llamado gausiana.pdf.
numgaus = np.random.normal(17,5,100)

plt.figure()
plt.hist(numgaus, bins=100)
plt.title(u"Gráfica: Histograma de números aleatorios en distribución gaussiana.")
plt.savefig("gausiana.pdf")

#Ejercicio 2.
#2a. Genere puntos aleatorios distribuidos uniformemente dentro de un cuadrado de lado 30.5. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado cuadrado.pdf. 
L1 = (30.5) * np.random.random(1000)
L2 = (30.5) * np.random.random(1000)

plt.figure(figsize=(5,5))
plt.scatter(L1,L2,color="black",marker='.')
plt.title(u"Gráfica: Puntos aleatorios en un cuadrado.")
plt.savefig("cuadrado.pdf")

#2b. Genere puntos aleatorios distribuidos uniformemente dentro de circulo de radio 23. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado circulo.pdf.
r = 23

P1 = (r*2) * np.random.random(1000) - 23
P2 = (r*2) * np.random.random(1000) - 23
P1p = []
P2p = []

for i in range(len(P1)):
    if(np.sqrt(P1[i]**2+P2[i]**2)<=r):
        P1p.append(P1[i])
        P2p.append(P2[i])

plt.figure(figsize=(5,5))
plt.scatter(P1p,P2p,color="black",marker='.')
plt.title(u"Gráfica: Puntos aleatorios en un círculo.")
plt.savefig("circulo.pdf")


#Ejercicio 4.
#Tome los puntos distribuidos aleatoriamente dentro del cuadrado y haga que cada punto siga una caminata aleatoria de 100 pasos. 
#La magnitud de los pasos de esta caminata debe seguir una distribucion gaussiana centrada en el punto y de sigma igual a 0.25.
#Implemente condiciones de frontera periodicas: si un punto se "sale" de cuadrado por un lado, "entra" por el otro.
numforpasos = np.random.normal(0,0.25,100)
ale = np.random.random(100) * 100
a = 0
for i in range(0,100):
    if(ale[i]<25):
        #arriba
        a = 1
    if(ale[i]>=25 and ale[i]<=50):
        #abajo
        a = 2
    if(ale[i]>50 and ale[i]<=75):
        #derecha
        a = 3
    if(ale[i]>75):
        #izquierda
        a = 4