#include <iostream>
#include <cmath>
using namespace std;

int * derivada(int a, int b, int n);
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
    cout<<"La derivada es: "<<derivada(a0,b0,n0)<<endl;
    cout<<lin_space(a0,b0,n0)<<endl;
    return 0;
}

int * derivada(int a, int b, int n){
    double h = (b-a)/n;
    float der[];
    int *point = der;
    return point;
}

int * lin_space(int a, int b, int n){
    double s = (b-a)/n;
    float lins[];
    float * pointer1 = lins;
    for(int i=0; i<=(b-a); i++){
        lins[i] = i * s;
        cout<<lins[i];
    }
    return pointer1;
}



//.   def funcion(x):
//.       return np.cos(x)
//.   
//.   n = 1000
//.   h = (2*np.pi)/n
//.   arr = np.linspace(0,2*np.pi,num=n)
//.   
//.   def central():
//.       der = []
//.       for i in arr:
//.           der.append((funcion(i+h/2)-funcion(i-h/2))/h)
//.       return der
