//Punto 2: Programa producto.

#include <iostream>
using namespace std;

int producto(int,int);

int main(){
    cout<<"El producto de a por b es: "<<producto(2,3.0)<<endl;
    return 0;
}

int producto(int a, int b){
    int c = a*b;
    return c;
}