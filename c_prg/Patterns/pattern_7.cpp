#include<bits/stdc++.h>
using namespace std;
void pattern(int n){
    for(int i=0;i<n;i++){
         for(int s=0;s<i;s++){
            cout<<"  ";
         }
         for(int j=0;j<(2*n-(2*i+1));j++){
            cout<<"* ";
         }
         for(int s=0;s<i;s++){
            cout<<"  ";
         }
        cout<<"\n";
    }
}
int main(){
    int n;
    cout<<"Enter number of lines";
    cin>>n;
    pattern(n);
    return 0;
}