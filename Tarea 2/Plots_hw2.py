import numpy as np
import matplotlib.pylab as plt

datax1 = np.genfromtxt("datax1.dat",delimiter=",")
datay1 = np.genfromtxt("datay1.dat",delimiter=",")
datax2 = np.genfromtxt("datax2.dat",delimiter=",")
datay2 = np.genfromtxt("datay2.dat",delimiter=",")
datax3 = np.genfromtxt("datax3.dat",delimiter=",")
datay3 = np.genfromtxt("datay3.dat",delimiter=",")
m_earth = 3.00273e-6

fig = plt.figure(figsize=(20,5))
a = fig.add_subplot(1,3,1)
a.plot(datax1[:,1],datay1[:,1],color="darkorange",label="dt = 0.1")
a.set_xlabel(u"Posición x.")
a.set_ylabel(u"Posición y.")
a.set_title(u"Rugen-Kutta: Posición en y vs. posición en x.")
a.legend(loc=1)

b = fig.add_subplot(1,3,2)
b.plot(datax2[:,1],datay2[:,1],color="darkorange",label="dt = 0.001")
b.set_xlabel(u"Posición x.")
b.set_ylabel(u"Posición y.")
b.set_title(u"Rugen-Kutta: Posición en y vs. posición en x.")
b.legend(loc=1)

c = fig.add_subplot(1,3,3)
c.plot(datax3[:,1],datay3[:,1],color="darkorange",label="dt = 0.0001")
c.set_xlabel(u"Posición x.")
c.set_ylabel(u"Posición y.")
c.set_title(u"Rugen-Kutta: Posición en y vs. posición en x.")
c.legend(loc=1)

plt.savefig("XY_met_dt.pdf")

fig1 = plt.figure(figsize=(20,5))
a1 = fig1.add_subplot(1,3,1)
a1.plot(datax1[:,2],datay1[:,2],color="c",label="dt = 0.1")
a1.set_xlabel(u"Velocidad en x.")
a1.set_ylabel(u"Velocidad en y.")
a1.set_title(u"Rugen-Kutta: Velocidad en y vs. velocidad en x.")
a1.legend(loc=1)

b1 = fig1.add_subplot(1,3,2)
b1.plot(datax2[:,2],datay2[:,2],color="c",label="dt = 0.001")
b1.set_xlabel(u"Velocidad en x.")
b1.set_ylabel(u"Velocidad en y.")
b1.set_title(u"Rugen-Kutta: Velocidad en y vs. velocidad en x.")
b1.legend(loc=1)

c1 = fig1.add_subplot(1,3,3)
c1.plot(datax3[:,2],datay3[:,2],color="c",label="dt = 0.0001")
c1.set_xlabel(u"Velocidad en x.")
c1.set_ylabel(u"Velocidad en y.")
c1.set_title(u"Rugen-Kutta: Velocidad en y vs. velocidad en x.")
c1.legend(loc=1)

plt.savefig("VxVy_met_dt.pdf")

def momentum(dats1,dats2):
    r = np.sqrt(dats1[:,1]**2,dats2[:,1]**2)
    v = np.sqrt(dats1[:,2]**2,dats2[:,2]**2)
    L = ([])
    s = (2*np.pi)/len(r)
    for i in range(len(r)):
        L.append(m_earth * v[i] * r[i] * np.sin(i*s))
    return L
  
fig2 = plt.figure(figsize=(20,5))
a2 = fig2.add_subplot(1,3,1)
a2.plot(datax1[:,0],momentum(datax1,datay1),color="indigo",label="dt = 0.1")
a2.set_ylabel(u"Momentum angular.")
a2.set_xlabel(u"Tiempo.")
a2.set_title(u"Rugen-Kutta: Momentum angular en función del tiempo.")
a2.legend(loc=1)

b2 = fig2.add_subplot(1,3,2)
b2.plot(datax2[:,0],momentum(datax2,datay2),color="indigo",label="dt = 0.001")
b2.set_ylabel(u"Momentum angular.")
b2.set_xlabel(u"Tiempo.")
b2.set_title(u"Rugen-Kutta: Momento angular en función del tiempo.")
b2.legend(loc=1)

c2 = fig2.add_subplot(1,3,3)
c2.plot(datax3[:,0],momentum(datax3,datay3),color="indigo",label="dt = 0.0001")
c2.set_ylabel(u"Momentum angular.")
c2.set_xlabel(u"Tiempo.")
c2.set_title(u"Rugen-Kutta: Momento angular en función del tiempo.")
c2.legend(loc=1)

plt.subplots_adjust(wspace = 0.3)
plt.savefig("Mome_met_dt.pdf")

def energia(dats1,dats2):
    r = np.sqrt(dats1[:,1]**2,dats2[:,1]**2)
    v = np.sqrt(dats1[:,2]**2,dats2[:,2]**2)
    k = (1/2) * m_earth * (v**2)
    u = m_earth * r
    return k + u

fig3 = plt.figure(figsize=(20,5))
a3 = fig3.add_subplot(1,3,1)
a3.plot(datax1[:,0],energia(datax1,datay1),color="orangered",label="dt = 0.1")
a3.set_xlabel(u"Tiempo.")
a3.set_ylabel(u"Energía total.")
a3.set_title(u"Rugen-Kutta: Energía total del sistema.")
a3.legend(loc=1)

b3 = fig3.add_subplot(1,3,2)
b3.plot(datax2[:,0],energia(datax2,datay2),color="orangered",label="dt = 0.001")
b3.set_xlabel(u"Tiempo.")
b3.set_ylabel(u"Energía total.")
b3.set_title(u"Rugen-Kutta: Energía total del sistema.")
b3.legend(loc=1)

c3 = fig3.add_subplot(1,3,3)
c3.plot(datax3[:,0],energia(datax3,datay3),color="orangered",label="dt = 0.0001")
c3.set_xlabel(u"Tiempo.")
c3.set_ylabel(u"Energía total.")
c3.set_title(u"Rugen-Kutta: Energía total del sistema.")
c3.legend(loc=1)

plt.savefig("Ener_met_dt.pdf")