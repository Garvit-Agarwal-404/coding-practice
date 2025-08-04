#include<bits/stdc++.h>
using namespace std;
int main(){
    map<string,int>m;
    m["apple"]=10;
    m["mango"]=40;
    m.insert({"yaeh",10});
    m.erase("yaeh");
    
    for(auto p:m){ 
        cout<<p.first<<" "<<p.second<<endl;
    }
    cout<<endl;
    cout<<m.count("yaeh");
    cout<<m.find("yaeh");
    return 0;
}