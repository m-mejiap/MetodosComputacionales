//Punto 3: Programa factorial.

#include <iostream>
using namespace std;

int factorial(int);

int main(){
    cout<<"El factorial del número dado es: "<<factorial(7)<<endl;
    return 0;
}

int factorial(int n){
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