#include<bits/stdc++.h>
using namespace std;
int prime_or_not(int n){
    if(n<=1) return -1;
    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            return 0;
        }
        
    }
    return 1;
}

int main(){
    int n;
    cout<<"Enter a number to check prime or not: ";
    cin>>n;
    int result=prime_or_not(n);
    if(result==-1){
        cout<<"The number is neither prime nor composite";
    }
    else if(result==0){
        cout<<"The number is not prime";
    }
    else if(result==1){
        cout<<"The number is prime";
    }
    return 0;

}

