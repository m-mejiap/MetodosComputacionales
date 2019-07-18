#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double h = 0.01;
double a = 0.0;
double b = 20;
int n_points = (b-a)/h;
float G = 6.674e-11*(pow(6.6846e-9,3)/(5.02785e-31*(pow(3.17098e-8,2))));
float m_sol = 1.989e30*5.02785e-31;
float r_ts = 1;

void Euler();
void Leap();
void Kutta();

int main(){
    Euler();
    Leap();
    Kutta();
    return 0;
}

void Euler(){
}

void Leap(){
}

void Kutta(){
    ofstream outfile;
    outfile.open("data.dat");
    double x[n_points]; //Tiempo.
    double y_1[n_points]; //Posición.
    double y_2[n_points]; //Velocidad.
    
    //Tome como condiciones iniciales x0 = 0.1163UA, y0 = 0.9772UA, vx0 = −6.35UA/yr y vy0 = 0.606UA/yr.
    
    x[0] = a; //Tiempo inicial.
    y_1[0] = sqrt(pow(0.1163,2)+pow(0.9772,2)); //Posición inicial.
    y_2[0] = sqrt(pow(-6.35,2)+pow(0.606,2)); //Velocidad inicial.
    
    outfile<<x[0]<<", "<<y_1[0]<<", "<<y_2[0]<<endl;
    
    for(int i=1; i<=n_points; i++){
        float x_old = x[i-1];
        float y1_old = y_1[i-1];
        float y2_old = y_2[i-1];
    
        float k_1_prime1 = y2_old;
        float k_1_prime2 = -(G*(m_sol/pow(r_ts,3)))*y1_old;
        
        float x1 = x_old + (h/2.0);
        float y1_1 = y1_old + (h/2.0) * k_1_prime1;
        float y2_1 = y2_old + (h/2.0) * k_1_prime2;
        float k_2_prime1 = y2_1;
        float k_2_prime2 = -(G*(m_sol/pow(r_ts,3)))*y1_1;
        
        float x2 = x_old + (h/2.0);
        float y1_2 = y1_old + (h/2.0) * k_2_prime1;
        float y2_2 = y2_old + (h/2.0) * k_2_prime2;
        float k_3_prime1 = y2_2;
        float k_3_prime2 = -(G*(m_sol/pow(r_ts,3)))*y1_2;    
        
        float x3 = x_old + h;
        float y1_3 = y1_old + h * k_3_prime1;
        float y2_3 = y2_old + h * k_3_prime2;
        float k_4_prime1 = y2_3;
        float k_4_prime2 = -(G*(m_sol/pow(r_ts,3)))*y1_3;    
        
        double average_k_1 = (1.0/6.0)*(k_1_prime1 + 2.0*k_2_prime1 + 2.0*k_3_prime1 + k_4_prime1);
        double average_k_2 = (1.0/6.0)*(k_1_prime2 + 2.0*k_2_prime2 + 2.0*k_3_prime2 + k_4_prime2);
        
        double x_new = x_old + h;
        double y_1_new = y1_old + h * average_k_1;
        double y_2_new = y2_old + h * average_k_2;
        
        outfile<<x_new<<", "<<y_1_new<<", "<<y_2_new<<endl;
        
        x[i] = x_new;
        y_1[i] = y_1_new;
        y_2[i] = y_2_new;
    } 
    
    outfile.close();
}