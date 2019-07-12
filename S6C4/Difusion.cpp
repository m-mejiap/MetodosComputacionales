#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

double L = 1.0;
double dx = 0.01;
double v = 0.0001;
double dt = (pow(dx,2)/v)*0.25;
double t_i = 0.0;
double t_f = 2600;
int n_points = 100;

int solve_1();
int solve_2();

int main(){
    cout<<solve_1()<<endl;
    cout<<solve_2()<<endl;
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
    
    outfile.close();
    
    //Futuroooo.  
    double futuro[n_points][n_points];
    int contador = 0;
    
    for(int t=1; t<=t_f; t++){
        for(int y=0; y<n_points; y++){
            for(int x=0; x<n_points; x++){
                if(x==0||x==99||y==0||y==99){
                    futuro[x][y] = 50;
                }
                else{
                    futuro[x][y] = ((v*dt)/pow(dx,2))*(inicial[x+1][y]+inicial[x-1][y]-4*inicial[x][y]+inicial[x][y+1]+inicial[x][y-1])+inicial[x][y];
                }
            }
        }
     
        if(contador==100){
            outfile.open("data1.dat");
            for(int y=0; y<n_points; y++){
                for(int x=0; x<n_points; x++){
                    outfile<<futuro[x][y]<<" ";
                }
            outfile<<endl;
            }
            outfile.close();
        }
        
        if(contador==2500){
            outfile.open("data2.dat");
            for(int y=0; y<n_points; y++){
                for(int x=0; x<n_points; x++){
                    outfile<<futuro[x][y]<<" ";
                }
            outfile<<endl;
            }
            outfile.close();
        }
  
        for(int k=0; k<n_points; k++){
            for(int l=0; l<n_points; l++){
                inicial[l][k] = futuro[l][k];
            }
        }
        contador++;
    }
    return 0;
}

int solve_2(){
    ofstream outfile;
    outfile.open("dataa.dat");
    
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
    
    outfile.close();
    
    //Futuroooo.  
    double futuro[n_points][n_points];
    int contador = 0;
    
    for(int t=1; t<=t_f; t++){
        for(int y=0; y<n_points; y++){
            for(int x=0; x<n_points; x++){
                if(x!=0||x!=99||y!=0||y!=99){
                    futuro[x][y] = ((v*dt)/pow(dx,2))*(inicial[x+1][y]+inicial[x-1][y]-4*inicial[x][y]+inicial[x][y+1]+inicial[x][y-1])+inicial[x][y];
                }
                if(x==0){
                    futuro[x][y] = futuro[98][y];
                }
                if(x==99){
                    futuro[x][y] = futuro[1][y];
                }
                if(y==0){
                    futuro[x][y] = futuro[x][98];
                }
                if(y==99){
                    futuro[x][y] = futuro[x][1];
                }
            }
        }
     
        if(contador==100){
            outfile.open("data11.dat");
            for(int y=0; y<n_points; y++){
                for(int x=0; x<n_points; x++){
                    outfile<<futuro[x][y]<<" ";
                }
            outfile<<endl;
            }
            outfile.close();
        }
        
        if(contador==2500){
            outfile.open("data22.dat");
            for(int y=0; y<n_points; y++){
                for(int x=0; x<n_points; x++){
                    outfile<<futuro[x][y]<<" ";
                }
            outfile<<endl;
            }
            outfile.close();
        }
  
        for(int k=0; k<n_points; k++){
            for(int l=0; l<n_points; l++){
                inicial[l][k] = futuro[l][k];
            }
        }
        contador++;
    }
    return 0;
}
