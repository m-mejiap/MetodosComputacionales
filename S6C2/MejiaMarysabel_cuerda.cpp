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
    for(int i=0; i<=n_points; i++){
        lins[i] = t_i + (i * s);
        inicial[i] = exp(-((lins[i]-0.3)*(lins[i]-0.3))/0.01);
    }
    
    double r = c * (dt/dx);
    
    double inicial[n_points];
    inicial[0] = 0;
    inicial[500] = A0;
    inicial[n_points] = 0;
    
    double finale[n_points];
    finale[0] = 0;
    finale[n_points] = 0;
    
    return 0;
}
