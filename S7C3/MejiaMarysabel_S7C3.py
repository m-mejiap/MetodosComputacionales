import numpy as np
import matplotlib.pylab as plt

#1. Lea los datos de resorte.dat y almacenelos.
data = np.genfromtxt("resorte(2).dat")

#2a. Definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo.
def modelo(a,gamma,omega,t):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

#2b. Definir una funcion que retorne la funcion de verosimilitud.
def verosimilitud(y_obs, y_model):
    X_2 = np.sum((y_obs-y_model)**2)
    return np.exp(-(1/2)*X_2)

#2c. Caminata.
#Condiciones iniciales.
aini=7.5
gammaini=0.6
omegaini=18.2

#Numero de pasos.
iteraciones=100000

m_viejo = modelo(aini,gammaini,omegaini,data[:,0])
p_almacena = np.zeros((iteraciones,3))
p_almacena[0,:] = [aini,gammaini,omegaini]
l_almacena = [verosimilitud(data[:,1],m_viejo)]
a_viejo = aini
gamma_viejo = gammaini
omega_viejo = omegaini

for i in range(1,iteraciones):
    a_nuevo = np.random.normal(a_viejo,1,1)[0]
    gamma_nuevo = np.random.normal(gamma_viejo,1,1)[0]
    omega_nuevo = np.random.normal(omega_viejo,1,1)[0]
    m_nuevo = modelo(a_nuevo,gamma_nuevo,omega_nuevo,data[:,0])
    
    alpha = verosimilitud(data[:,1],m_nuevo)/verosimilitud(data[:,1],m_viejo)
    
    if(alpha>=1):
        p_almacena[i,:] = [a_nuevo,gamma_nuevo,omega_nuevo]
    if(alpha<1):
        beta = np.random.random(1)[0]
        if(beta<alpha):
            p_almacena[i,:] = [a_nuevo,gamma_nuevo,omega_nuevo]
        if(beta>alpha):
            p_almacena[i,:] = [a_viejo,gamma_viejo,omega_viejo]
    
    l_almacena.append(verosimilitud(data[:,1],m_nuevo))
    a_viejo = a_nuevo
    gamma_viejo = gamma_nuevo
    omega_viejo = omega_nuevo
    
#for i in range(1,iteraciones):
#    a_nuevo = np.random.normal(a_viejo,0.01,1)[0]
#    gamma_nuevo = np.random.normal(gamma_viejo,0.01,1)[0]
#    omega_nuevo = np.random.normal(omega_viejo,0.05,1)[0]
#    m_nuevo = modelo(a_nuevo,gamma_nuevo,omega_nuevo,data[:,0])
#    
#    alpha = verosimilitud(data[:,1],m_nuevo)/verosimilitud(data[:,1],m_viejo)
#    
#    if(alpha>=1):
#        p_almacena[i,:] = [a_nuevo,gamma_nuevo,omega_nuevo]
#        a_viejo = a_nuevo
#        gamma_viejo = gamma_nuevo
#        omega_viejo = omega_nuevo
#        l_almacena.append(verosimilitud(data[:,1],m_nuevo))
#    if(alpha<1):
#        beta = np.random.random(1)[0]
#        if(beta<alpha):
#            p_almacena[i,:] = [a_nuevo,gamma_nuevo,omega_nuevo]
#            a_viejo = a_nuevo
#            gamma_viejo = gamma_nuevo
#            omega_viejo = omega_nuevo
#            l_almacena.append(verosimilitud(data[:,1],m_nuevo))
#        if(beta>alpha):
#            p_almacena[i,:] = [a_viejo,gamma_viejo,omega_viejo]
#            l_almacena.append(verosimilitud(data[:,1],m_viejo))

#2d. Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."
loc = (np.argmax(l_almacena))
print("Los mejores parametros son:",p_almacena[loc])

#2f. Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf
plt.figure()
plt.plot(data[:,0],data[:,1],color="black",label="Datos originales.")
plt.plot(data[:,0],modelo(p_almacena[loc][0],p_almacena[loc][1],p_almacena[loc][2],data[:,0]),color="grey",label="Datos originales.")
plt.xlabel("Tiempo.")
plt.ylabel(u"Posición en x.")
plt.title(u"Gráfica: Estimación bayesiana.")
plt.legend()
plt.savefig("resorte.pdf")
