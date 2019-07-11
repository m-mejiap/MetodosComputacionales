#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double L = 1.0;
double dx = 0.05;
double c = 300.0;
double dt = (dx/c)*0.25;
double t_i = 0.0;
double t_f = 0.1;
double A0 = 0.01;
int n_points = 1000;

int solve_1();
int solve_2();
int solve_3();

int main(){
    cout<<solve_1()<<endl;
    cout<<solve_2()<<endl;
    cout<<solve_3()<<endl;
    return 0;
}

int solve_1(){
    ofstream outfile;
    outfile.open("data.dat");
    double s = L/n_points;
    double lins[n_points];
    lins[0] = 0;
    lins[n_points] = L;
    
    //Condición inicial.
    double inicial[n_points];
    inicial[0] = 0;
    inicial[n_points/2] = A0;
    inicial[n_points] = 0;
    
    outfile<<lins[0]<<","<<inicial[0]<<endl;
    
    for(int i=1; i<=n_points-1; i++){
        lins[i] = t_i + (i * s); //Aquí se genran los valores de x.
        if(i<n_points/2){
            inicial[i] = (A0/(L/2))*(lins[i]);
        }
        if(i>n_points/2){
            inicial[i] = -(A0/(L/2))*(lins[i])+(2*A0);
        }
        outfile<<lins[i]<<","<<inicial[i]<<endl;
    }
    
    outfile<<lins[n_points]<<","<<inicial[n_points]<<endl;
    
    //Primer paso.
    double siguiente[n_points];
    siguiente[0] = 0;
    siguiente[n_points] = 0;
    
    for(int i=1; i<=n_points-1; i++){
        siguiente[i] = (pow(c,2)*pow(dt,2)/(2*pow(dx,2)))*(inicial[i+1]+inicial[i-1]-2*inicial[i])+inicial[i];
    }
    
    //Futuroooo.    
    double futuro[n_points];
    futuro[0] = 0;
    futuro[n_points] = 0;
    int contador = 0;
    
    for(int j=2; j<=20000; j++){
        for(int i=1; i<=n_points-1; i++){
          futuro[i] = ((pow(c,2)*pow(dt,2)/pow(dx,2))*(siguiente[i+1]+siguiente[i-1]-2*siguiente[i]))-inicial[i]+(2*siguiente[i]);
        }
        if(contador==600||contador==1200||contador==1800||contador==2400||contador==3000||contador==3600){
            outfile<<lins[0]<<","<<futuro[0]<<endl;
            for(int i=1; i<=n_points-1; i++){
                outfile<<lins[i]<<","<<futuro[i]<<endl;
            }
            outfile<<lins[n_points]<<","<<futuro[n_points]<<endl;
        }
        for(int k=1; k<=n_points-1; k++){
            inicial[k] = siguiente[k];
            siguiente[k] = futuro[k];
        }
        contador++;
    }
    outfile.close();
    return 0;
}

int solve_2(){
    ofstream outfile;
    outfile.open("data2.dat");
    double s = L/n_points;
    double lins[n_points];
    lins[0] = 0;
    lins[n_points] = L;
    
    //Condición inicial.
    double inicial[n_points];
    inicial[0] = 0;
    inicial[n_points/2] = A0;
    
    outfile<<lins[0]<<","<<inicial[0]<<endl;
    
    for(int i=1; i<=n_points; i++){
        lins[i] = t_i + (i * s); //Aquí se genran los valores de x.
        if(i<n_points/2){
            inicial[i] = (A0/(L/2))*(lins[i]);
        }
        if(i>n_points/2 && i<n_points){
            inicial[i] = -(A0/(L/2))*(lins[i])+(2*A0);
        }
        if(i==n_points){
            inicial[i] = inicial[i-1];
        }
        outfile<<lins[i]<<","<<inicial[i]<<endl;
    }
    
    //Primer paso.
    double siguiente[n_points];
    siguiente[0] = 0;
    
    for(int i=1; i<=n_points; i++){
        if(i<n_points){
            siguiente[i] = (pow(c,2)*pow(dt,2)/(2*pow(dx,2)))*(inicial[i+1]+inicial[i-1]-2*inicial[i])+inicial[i];
        }
        if(i==n_points){
            siguiente[i] = siguiente[i-1];
        }
    }
    
    //Futuroooo.    
    double futuro[n_points];
    futuro[0] = 0;
    int contador = 0;
    
    for(int j=2; j<=20000; j++){
        for(int i=1; i<=n_points; i++){
            if(i<n_points){
         futuro[i] = ((pow(c,2)*pow(dt,2)/pow(dx,2))*(siguiente[i+1]+siguiente[i-1]-2*siguiente[i]))-inicial[i]+(2*siguiente[i]);
            }
            if(i==n_points){
                futuro[i] = futuro[i-1];
            }
        }
        if(contador==600||contador==1200||contador==1800||contador==2400||contador==3000||contador==3600){
            outfile<<lins[0]<<","<<futuro[0]<<endl;
            for(int i=1; i<=n_points; i++){
                outfile<<lins[i]<<","<<futuro[i]<<endl;
            }
        }
        for(int k=1; k<=n_points; k++){
            inicial[k] = siguiente[k];
            siguiente[k] = futuro[k];
        }
        contador++;
    }
    outfile.close();
    return 0;
}

int solve_3(){
    ofstream outfile;
    outfile.open("data3.dat");
    double s = L/n_points;
    double lins[n_points];
    lins[0] = 0;
    lins[n_points] = L;
    
    //Condición inicial.
    double inicial[n_points];
    inicial[0] = 0;
    inicial[n_points/2] = A0;
    
    outfile<<lins[0]<<","<<inicial[0]<<endl;
    
    for(int i=1; i<=n_points; i++){
        lins[i] = t_i + (i * s); //Aquí se genran los valores de x.
        if(i<n_points/2){
            inicial[i] = (A0/(L/2))*(lins[i]);
        }
        if(i>n_points/2 && i<n_points){
            inicial[i] = -(A0/(L/2))*(lins[i])+(2*A0);
        }
        if(i==n_points){
            inicial[i] = 0;
        }
        outfile<<lins[i]<<","<<inicial[i]<<endl;
    }
    
    //Primer paso.
    double siguiente[n_points];
    siguiente[0] = 0;
    
    for(int i=1; i<=n_points; i++){
        if(i<n_points){
            siguiente[i] = (pow(c,2)*pow(dt,2)/(2*pow(dx,2)))*(inicial[i+1]+inicial[i-1]-2*inicial[i])+inicial[i];
        }
        if(i==n_points){
            siguiente[i] = A0*sin((3*c*1*dt*3.1416)/L);
        }
    }
    
    //Futuroooo.    
    double futuro[n_points];
    futuro[0] = 0;
    int contador = 0;
    
    for(int j=2; j<=20000; j++){
        for(int i=1; i<=n_points; i++){
            if(i<n_points){
         futuro[i] = ((pow(c,2)*pow(dt,2)/pow(dx,2))*(siguiente[i+1]+siguiente[i-1]-2*siguiente[i]))-inicial[i]+(2*siguiente[i]);
            }
            if(i==n_points){
                futuro[i] = A0*sin((3*c*j*dt*3.1416)/L);
            }
        }
        if(contador==600||contador==1200||contador==1800||contador==2400||contador==3000||contador==3600){
            outfile<<lins[0]<<","<<futuro[0]<<endl;
            for(int i=1; i<=n_points; i++){
                outfile<<lins[i]<<","<<futuro[i]<<endl;
            }
        }
        for(int k=1; k<=n_points; k++){
            inicial[k] = siguiente[k];
            siguiente[k] = futuro[k];
        }
        contador++;
    }
    outfile.close();
    return 0;
}
