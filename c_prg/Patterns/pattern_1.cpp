#include<bits/stdc++.h>
using namespace std;
void pattern_1(int n)
{   
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<"* ";
        }
        cout<<"\n";
    }
}
  
int main(){
    int n;
    cout<<"Enter number of lines";
    cin>>n;
    pattern_1(n);
    return 0;
}