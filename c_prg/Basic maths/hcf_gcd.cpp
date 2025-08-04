#include<bits/stdc++.h>
using namespace std;
int hcf(int n1,int n2){
    for(int i=min(n1,n2);i>=1;i--){
        if(n1%i==0 && n2%i==0){
            return i;
        }
    }
}
int main(){
    int n1,n2;
    cout<<"Enter two numbers to check their hcf: ";
    cin>>n1>>n2;
    cout<<"HCF of "<<n1<<" and "<<n2<<" is "<<hcf(n1,n2);
    return 0;
}