#include<bits/stdc++.h>
using namespace std;
int main(){
    stack<int>s;
    s.push(1);
    s.push(2);
    s.emplace(3);
    cout<<"Top="<<s.top()<<endl;
    
    return 0;
}