#include<bits/stdc++.h>
using namespace std;
void pattern(int n){
    for(int i=0;i<n;i++){
        for(int s=n;s>i;s--){ // for space
            cout<<"  ";
        }
        for(int j=0;j<2*i+1;j++){ //for star
            cout<<"* ";
        }
        for(int s=n;s>i;s--){ //for space
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