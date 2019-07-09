#include <iostream>
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
    double r = c * (dt/dx);
    
    double inicial[n_points];
    inicial[0] = 0;
    inicial[500] = A0;
    inicial[n_points] = 0;
    
    double finale[n_points];
    finale[0] = 0;
    finale[n_points] = 0;
    
    double s = 0.001;
    double lins[n_points];
    for(int i=0; i<=n_points; i++){
        lins[i] = t_i + (i * s);
        cout<<inicial[i]<<endl;
    }

    return 0;
}