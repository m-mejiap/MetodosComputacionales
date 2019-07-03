#include <iostream>
using namespace std;

int derivada(int a, int b, int n);
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
    cout<<derivada(a0,b0,n0)<<endl;
    return 0;
}

int derivada(int a, int b, int n){
    return 0;
}