#include<bits/stdc++.h>
using namespace std;
void divs(int n){
    for(int i=1;i<=n/2;i++){
        if(n%i==0){
            cout<<i<<", ";
        }
    }
}
void optimized_divs(int n){
    vector<int>lst;
    for(int i=1;i*i<=n;i++){
        if(n%i==0){
            lst.push_back(i);
            if(i!=n/i){
                lst.push_back(n/i);
            }
        }
    }
    sort(lst.begin(),lst.end());
   for(auto it=lst.begin();it!=lst.end();it++){
    cout<<*(it)<<" ";
   }

}
int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    cout<<"The divisors of "<<n<<" are: ";
    
    optimized_divs(n);
    return 0;
}