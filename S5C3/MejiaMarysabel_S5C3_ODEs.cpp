//Usted debe calcular la posición y velocidad en función del tiempo de una masa atada a un resorte que se mueve sobre un plano sin friccion. La ecuación que debe resolver es: m*d2x(t)/dt2 = −kx(t) Donde x(t) es la posicón de la masa en función del tiempo t, m es la masa del cuerpo y k la constante del resorte.
//Tome m = 2kg, k = 300N/m y suponga que en el tiempo t = 0 el resorte tiene velocidad cero y está elongado en x(t=0)=0.1m con respecto a la posición de equilibrio (tome la posición de equilibrio en x=0).

#include <fstream>
#include <iostream>
using namespace std;

//a) Usando el método de Leap Frog o el de Runge Kutta de 4to orden resuleva la ecuación diferencial de segundo orden.

double h = 0.01;
double a = 0.0;
double b = 5.0;
double m = 2.0;
double k = 300;
int n_points = (b-a)/h;
int solve2_Runge();

int main(){
    cout<<solve2_Runge()<<endl;
    return 0;
}

int solve2_Runge(){
    double x[n_points];
    double y_1[n_points]; //Posición.
    double y_2[n_points]; //Velocidad.
    
    x[0] = a; //Condicion inicial.
    y_1[0] = 0.1; //Condicion inicial 1.
    y_2[0] = 0.0; //Condicion inicial 2.
    cout<<x[0]<<", "<<y_1[0]<<", "<<y_2[0]<<endl;
    
    double *pointer1;
    pointer1 = y_1;
    
    double *pointer2;
    pointer2 = y_2;
    
    for(int i=1;i<=n_points;i++){ 
        double k1_1 = h * (y_2[i-1]);
        double k2_1 = h * (y_2[i-1]-(0.5*k1_1));
        double k3_1 = h * (y_2[i-1]-(0.5*k2_1));
        double k4_1 = h * (y_2[i-1]-k3_1);
        
        double average_k_1 = (1.0/6.0)*(k1_1 + 2.0*k2_1 + 2.0*k3_1 + k4_1);
        
        x[i] = x[i-1] + h;
        y_1[i] = y_1[i-1] + average_k_1;
        
        double k1_2 = h * (-(k/m)*y_1[i-1]);
        double k2_2 = h * (-(k/m)*y_1[i-1]-(0.5*k1_2));
        double k3_2 = h * (-(k/m)*y_1[i-1]-(0.5*k2_2));
        double k4_2 = h * (-(k/m)*y_1[i-1]-k3_2);
        
        double average_k_2 = (1.0/6.0)*(k1_2 + 2.0*k2_2 + 2.0*k3_2 + k4_2);
        
        y_2[i] = y_2[i-1] + average_k_2;
        cout<<x[i]<<", "<<y_1[i]<<", "<<y_2[i]<<endl;
    }
    
    return 0;
}

//b) Calcule la posición de la masa en función del tiempo hasta un tiempo final de t = 5s e imprima en consola el tiempo t, la velocidad y la posición de la masa.

//Escriba un script en python llamado ApellidoNombre_S5C3_plots.py que Grafique con matplotlib dicha posición en función del tiempo y Guarde la gráfica obtenida en ApellidoNombreResorte.pdf
//Escriba un Makefile llamado ApellidoNombre_S5C3.mk que genere la grafica, datos y maneje las dependencias, etc...