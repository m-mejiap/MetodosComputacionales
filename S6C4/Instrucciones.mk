#Makefile necesario para correr el ejercicio de la ecuación de difusión en 2D.

plots_difusion.png : data.dat Plots_Difusion.py
	python Plots_Difusion.py

data.dat : a.out
	./a.out
    
data1.dat : a.out
	./a.out
    
data2.dat : a.out
	./a.out
    
dataa.dat : a.out
	./a.out
    
data11.dat : a.out
	./a.out
    
data22.dat : a.out
	./a.out

a.out : Difusion.cpp
	g++ Difusion.cpp