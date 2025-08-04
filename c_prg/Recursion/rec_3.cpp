#include<bits/stdc++.h>
using namespace std;
void rec(int i,int n){
    if(n<i){
        return;
    }
    cout<<n<<" ";
    rec(i,n-1);
}
int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    rec(1,n);
}