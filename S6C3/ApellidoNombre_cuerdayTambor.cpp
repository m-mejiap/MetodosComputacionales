#include <iostream>
#include <cmath>
using namespace std;

double L = 1.0;
double dt = 0.000005;
double dx = 0.005;
double c = 300.0;
double t_i = 0.0;
double t_f = 0.1;
double A0 = 0.01;
int n_points = 1000;

int solve_1();

int main(){
    cout<<solve_1()<<endl;
    return 0;
}

int solve_1(){
    double s = L/n_points;
    double lins[n_points];
    double inicial[n_points];
    
    inicial[0] = 0;
    inicial[n_points/2] = A0;
    inicial[n_points] = 0;
    cout<<lins[0]<<","<<inicial[0]<<endl;
    
    for(int i=1; i<=n_points-1; i++){
        lins[i] = t_i + (i * s);
        if(i<n_points/2){
            inicial[i] = (A0/(L/2))*(lins[i]);
        }
        if(i>n_points/2){
            inicial[i] = -(A0/(L/2))*(lins[i])+(2*A0);
        }
        //inicial[i] = (pow(c,2)*pow(dt,2)/pow(dx,2))*(inicial[i+1]+inicial[i-1]-2*inicial[i]);
        cout<<lins[i]<<","<<inicial[i]<<endl;
    }
    
    cout<<lins[n_points]<<","<<inicial[n_points]<<endl;
    
    return 0;
}
