#Makefile.
    
plots.png : data.dat MejiaMarysabel_S5C3_plots.py
	python Plots_cuerdayTambor.py
    
data.dat : a.out
	g++ MejiaMarysabel_S5C3_ODEs.cpp
	./a.out > data.dat
    
a.out : MejiaMarysabel_CuerdayTambor.cpp
	g++ MejiaMarysabel_S5C3_ODEs.cpp