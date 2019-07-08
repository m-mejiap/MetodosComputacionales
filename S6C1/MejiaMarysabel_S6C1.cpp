#include <iostream>
using namespace std;

int N_x = 80;
int b = 2;
int a = 0;
int func();

int main(){
    cout<<func()<<endl;
    return 0;
}

int func(){
    double arr[N_x];
    double lins[N_x];
    double s = 0.025;

    for(int i=0; i<=N_x; i++){
        lins[i] = a + (i * s);
    }        
    for(int i=0;i<=N_x;i++){
        if(lins[i]>=0.75&&lins[i]<=1.75){
            arr[i]=2;
            cout<<lins[i]<<", "<<arr[i]<<endl;
        }
        else{
            arr[i]=0;
            cout<<lins[i]<<", "<<arr[i]<<endl;
        }    
    }
    return 0;
}

//.    n_x = 80
//.    n_t = 100
//.    
//.    c = 1.0
//.    nu = 0.3
//.    sigma = 0.2 #sigma is a parameter to ensure \alpha\nu < 0.5
//.    
//.    x = linspace(0, 2.0, n_x)
//.    dx = x[1]-x[0]
//.    
//.    
//.    dt = sigma*dx**2/nu #dt is defined using sigma
//.    alpha = dt/dx**2
//.    print dt
//.    
//.    u = ones(n_x)
//.    
//.    u[where((x<1.25) & (x>0.75))] = 2.0
//.        
//.    plot(x,u)
//.        
//.    for n in range(n_t):  # loop over time
//.        u_past = u.copy() 
//.        for i in range(1,n_x-1): #loop over space
//.            u[i] = nu * alpha * u_past[i+1]  + (1.0 - 2.0*nu*alpha)*u_past[i] + nu*alpha*u_past[i-1]
//.            
//.    plot(x,u)
