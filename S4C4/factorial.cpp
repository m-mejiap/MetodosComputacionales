//Punto 3: Programa factorial.

#include <iostream>
using namespace std;

float factorial(int);

int main(){
    cout<<"El factorial de 7  es: "<<factorial(7)<<endl;
    cout<<"El factorial de 77  es: "<<factorial(77)<<endl;
    return 0;
}

float factorial(int n){
    int i;
    int c;
    c = n;
    i = n - 1;
    while(i > 0)
    {
        c = c * (i);
        i = i - 1;
    }
    return c;
}