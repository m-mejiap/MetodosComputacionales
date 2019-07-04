#include <iostream>
#include <cmath>
using namespace std;

double * lin_space(int a, int b, int n);
double * funcion(double x[], int n);
double * derivada(double a[], double b[]);
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
    
    cout<<lin_space(a0,b0,n0)<<endl;
    cout<<funcion(lin_space(a0,b0,n0),n0)<<endl;
    cout<<derivada(lin_space(a0,b0,n0),funcion(lin_space(a0,b0,n0),n0))<<endl;
    return 0;
}

double * lin_space(int a, int b, int n){
    double s = (b-a)/n;
    double lins[n];
    double * pointer1 = lins;
    for(int i=0; i<=n; i++){
        lins[i] = a + (i * s);
        //cout<<lins[i]<<endl;
    }
    return pointer1;
}

double * funcion(double x[], int n){
    double coseno[n];
    double * pointer2 = coseno;
    for(int i=0; i<=n; i++){
        coseno[i] = cos(x[i]);
        //cout<<x[i]<<","<<coseno[i]<<endl;
    }
    return pointer2;
}

double * derivada(double x2[], double fx[]){
    double fxh[n0-1];
    for(int i=1; i<=n0; i++){
        fxh[i] = fx[i];
    }
    double h = x2[1]-x2[0];
    
    double uhh[n0-1];
    for(int i=0; i<=n0-1; i++){
        uhh[i] = fxh[i] - fx[i];
    }
    
    double der[n0-1];
    double *point = der;
    for(int i=0; i<=n0-1; i++){
        der[i] = uhh[i]/h;
    }
    return point;
}