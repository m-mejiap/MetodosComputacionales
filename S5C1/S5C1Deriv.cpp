#include <iostream>
#include <cmath>
using namespace std;

double * lin_space(int a, int b, int n);
double * funcion(double x[], int n);
double * derivada(int a, int b, int n);
int a0;
int b0;
int n0;

int main(){
    cout<<"Inicio del intervalo: ";
    cin>>a0;
    cout<<"Final del intervalo: ";
    cin>>b0;
    cout<<"Número de puntos: ";
    cin>>n0;
    cout<<endl;
    cout<<lin_space(a0,b0,n0)<<endl;
    double x0[n0] = lin_space(a0,b0,n0);
    cout<<funcion(x0,n0)<<endl;
    cout<<derivada(a0,b0,n0)<<endl;
    return 0;
}

double * lin_space(int a, int b, int n){
    double s = (b-a)/n;
    double lins[n];
    double * pointer1 = lins;
    for(int i=0; i<=n; i++){
        lins[i] = a + (i * s);
        cout<<lins[i]<<endl;
    }
    return pointer1;
}

double * funcion(double x[], int n){
    double coseno[n];
    double * pointer2 = coseno;
    for(int i=0; i<=n; i++){
        coseno[i] = 1;
        cout<<x[i]<<endl;
    }
    return pointer2;
}

double * derivada(int a, int b, int n){
    double h = (b-a)/n;
    double der[n];
    double *point = der;
    return point;
}

//coseno[i]<<","<<
//x = np.array([])
//x = np.append(x, np.genfromtxt('datosfun.dat',usecols=0))
//fx = np.array([])
//fx = np.append(fx, np.genfromtxt('datosfun.dat',usecols=1))
//
//fxh = np.array([])
//fxh = np.append(fxh, fx[1:])
//h = np.absolute(x[1]-x[0])
//uhh =  fxh - fx[0:-1]
//derivada = uhh/h
