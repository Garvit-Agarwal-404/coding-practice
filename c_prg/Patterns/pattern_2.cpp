#include<bits/stdc++.h>
using namespace std;
void pattern(int n){
    for(int i=1;i<=n;i++){ //or int i=1;i<n
        for(int j=0;j<i;j++){ //or int j=0;j<i+1
            cout<<"* ";
        }
        cout<<"\n";
    }
}
int main()
{
    int n;
    cout<<"Enter number of lines";
    cin>>n;
    pattern(n);
    return 0;
}