#include<bits/stdc++.h>
using namespace std;
void pattern(int n){
    for(int i=0;i<n;i++){
        for(int j=1;j<=i+1;j++){
            cout<<j<<" ";
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