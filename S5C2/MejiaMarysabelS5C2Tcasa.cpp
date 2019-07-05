//Solucion de ecuaciones diferenciales ordinarias.
//Implemente el metodo de Euler y el de Runge Kutta de 4to orden para resolver la ecuación dy/dx = -y en el intervalo 0<x<2 con condicion inicial y(0)=1.

#include <fstream>
#include <iostream>
using namespace std;

//Metodo de Euler.

double h = 0.01;
double a = 0.0;
double b = 2.0;
int n_points = (b-a)/h;
double * solve_Euler();
double * solve_Runge();

int main(){
    cout<<solve_Euler()<<endl;
    cout<<solve_Runge()<<endl;
    return 0;
}

double * solve_Euler(){
    double x[n_points];
    double y[n_points];
    
    x[0] = a; //Condicion inicial.
    y[0] = 1.0; //Condicion inicial.

    double *pointer;
    pointer = y;
    
    for(int i=1;i<=n_points;i++){
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + h * (-y[i-1]);
        cout<<x[i]<<", "<<y[i]<<endl;
    }
    return pointer;
}

//Metodo de Runge Kutta de 4to orden.

double * solve_Runge(){
    double x[n_points];
    double y[n_points];
    
    x[0] = a; //Condicion inicial.
    y[0] = 1.0; //Condicion inicial.
    
    double *pointer;
    pointer = y;
    
    for(int i=1;i<=n_points;i++){ 
        double k1 = h * (-y[i-1]);
        double k2 = h * (-y[i-1]-(0.5*k1));
        double k3 = h * (-y[i-1]-(0.5*k2));
        double k4 = h * (-y[i-1]-k3);
        
        double average_k = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);
        
        x[i] = x[i-1] + h;
        y[i] = y[i-1] + average_k;
        cout<<x[i]<<", "<<y[i]<<endl;
    }
    return pointer;
}