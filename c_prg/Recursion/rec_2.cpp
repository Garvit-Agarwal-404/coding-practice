#include<bits/stdc++.h>
using namespace std;
void rec(int i,int n){
    if(i>n){
        return;
    }
    cout<<i<<" ";
    rec(i+1,n);
}
int main(){
    int n;
    cout<<"Enter a number";
    cin>>n;
    rec(1,n);
}