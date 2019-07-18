#Escriba un Makefile llamado ApellidoNombre_S5C3.mk que genere la grafica, datos y maneje las dependencias, etc...

MejiaMarysabelResorte.png : data.dat MejiaMarysabel_S5C3_plots.py
	python MejiaMarysabel_S5C3_plots.py
      
data.dat : MejiaMarysabel_S5C3_ODEs.cpp
	g++ MejiaMarysabel_S5C3_ODEs.cpp
	./a.out > data.dat
    
