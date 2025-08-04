#include<bits/stdc++.h>
using namespace std;
void naam(int n,string s){
    if(n==0){
        return;
    }
    cout<<s<<" ";
    naam(n-1,s);

}
int main(){
    cout<<"Enter number of times you want to print";
    int n;
    cin>>n;
    naam(n,"Garvit");
}