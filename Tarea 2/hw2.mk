FFtIm.pdf ImProceso.pdf ImHybrid.pdf XY_met_dt.pdf VxVy_met_dt.pdf Mome_met_dt.pdf Ener_met_dt.pdf: Fourier.py datax1.dat datay1.dat datax2.dat datay2.dat datax3.dat datay3.dat Plots_hw2.py
	python Fourier.py
	python Plots_hw2.py
    
datax1.dat datay1.dat datax2.dat datay2.dat datax3.dat datay3.dat : a.out
	./a.out
    
a.out : ODEs.cpp
	g++ ODEs.cpp