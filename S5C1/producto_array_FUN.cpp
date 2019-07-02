#include <iostream>
using namespace std;

int * p_elemento(int in1[], int in2[]);
int p_punto(int in1[], int in2[]);

int main(){
    int a1[5] = {1,2,3,4,5};
    int a2[5] = {10,20,30,40,50};
    cout<<"El producto elemento a elemento de los dos arreglos es: ";
    for(int i=0; i<5; i++){
        if (i<4){
            cout<<p_elemento(a1,a2)[i]<<",";
        }
        else{
            cout<<p_elemento(a1,a2)[i]<<".";
        }
    }
    cout<<endl;
    cout<<"El producto punto de los elementos es es: "<< p_punto(a1,a2) << "." <<endl;
    return 0;
}

int * p_elemento(int in1[],int in2[]){
    int producto[5];
    int *point;
    point = producto;
    for(int i=0; i<5; i++){
        producto[i] = in1[i] * in2[i];
    }
    return point;
}

int p_punto(int in1[],int in2[]){
    int producto = 0;
    for(int i=0; i<5; i++){
        producto = producto + (in1[i] * in2[i]);
    }
    return producto;
}