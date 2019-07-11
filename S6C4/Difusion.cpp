#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double L = 1.0;
double dx = 0.01;
double v = 0.0001;
double dt = (dx/v)*0.25;
double t_i = 0.0;
double t_f = 2500;
int n_points = 100;

int solve_1();

int main(){
    cout<<solve_1()<<endl;
    return 0;
}

int solve_1(){
    ofstream outfile;
    outfile.open("data.dat");
    
    //Condición inicial.
    double inicial[n_points][n_points];
    
    for(int y=0; y<n_points; y++){
        for(int x=0; x<n_points; x++){
            if(x<20||x>40){
                inicial[x][y] = 50;
            }
            else if(y<40||y>60){
                inicial[x][y] = 50;
            }
            else{
                inicial[x][y] = 100;
            }
            outfile<<inicial[x][y]<<" ";
        }
        outfile<<endl;
    }
    
 // //Primer paso.
 // double siguiente[n_points];
 // siguiente[0] = 0;
 // siguiente[n_points] = 0;
 // 
 // for(int i=1; i<=n_points-1; i++){
 //     siguiente[i] = (pow(c,2)*pow(dt,2)/(2*pow(dx,2)))*(inicial[i+1]+inicial[i-1]-2*inicial[i])+inicial[i];
 // }
 // 
 // //Futuroooo.    
 // double futuro[n_points];
 // futuro[0] = 0;
 // futuro[n_points] = 0;
 // int contador = 0;
 // 
 // for(int j=2; j<=20000; j++){
 //     for(int i=1; i<=n_points-1; i++){
 //       futuro[i] = ((pow(c,2)*pow(dt,2)/pow(dx,2))*(siguiente[i+1]+siguiente[i-1]-2*siguiente[i]))-inicial[i]+(2*siguiente[i]);
 //     }
 //     if(contador==600||contador==1200||contador==1800||contador==2400||contador==3000||contador==3600){
 //         outfile<<lins[0]<<","<<futuro[0]<<endl;
 //         for(int i=1; i<=n_points-1; i++){
 //             outfile<<lins[i]<<","<<futuro[i]<<endl;
 //         }
 //         outfile<<lins[n_points]<<","<<futuro[n_points]<<endl;
 //     }
 //     for(int k=1; k<=n_points-1; k++){
 //         inicial[k] = siguiente[k];
 //         siguiente[k] = futuro[k];
 //     }
 //     contador++;
 // }
 // outfile.close();
    
    return 0;
}
