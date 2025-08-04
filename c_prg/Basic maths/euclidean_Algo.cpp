#include<bits/stdc++.h>
using namespace std;
int euclid_gcd(int n1,int n2){                  // normal function 
    while(n2!=0){
        int temp=n2;
        n2=n1%n2; 
        n1=temp;

    }
    return n1;
}
int euclid_gcd_recusrsive(int a,int b){         // recursive function
    if(b==0) return a;
    euclid_gcd_recusrsive(b,a%b);
}
int main(){
    int n1,n2;
    cout<<"Enter two numbers to check their gcd: ";
    cin>>n1>>n2;
    cout<<"GCD of "<<n1<<" and "<<n2<<" is "<<euclid_gcd_recusrsive(n1,n2);
    return 0;
}