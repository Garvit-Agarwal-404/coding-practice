#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int>v={1,2,3,4,5};
    vector<int>::iterator it;
    for(it=v.begin();it!=v.end();it++){
        cout<<*(it)<<" ";
    }
    cout<<endl;
    for(auto it_1=v.rbegin();it_1!=v.rend();it_1++){
        cout<<*(it_1)<<" ";
    }
    cout<<endl;
    cout<<v.front()<<endl<<v.back();
    cout<<endl<<*(v.begin())<<endl<<*(v.end()-1);

    
    return 0;
}
