#Makefile.

plots.png : data.dat Plots_cuerdayTambor.py
	python Plots_cuerdayTambor.py

data.dat : a.out
	./a.out
    
data2.dat : a.out
	./a.out
    
data3.dat : a.out
	./a.out

a.out : MejiaMarysabel_CuerdayTambor.cpp
	g++ MejiaMarysabel_CuerdayTambor.cpp
