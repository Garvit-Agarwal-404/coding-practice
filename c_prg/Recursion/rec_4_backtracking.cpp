#include<bits/stdc++.h>
using namespace std;
void rec(int n){
    if(n<1){
        return;
    }
    rec(n-1);
    cout<<n<<" ";
}
int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    rec(n);

}