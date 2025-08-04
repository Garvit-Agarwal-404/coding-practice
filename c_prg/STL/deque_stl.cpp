#include<bits/stdc++.h>
using namespace std;
int main(){
    deque<int>d={1,2,3};
    d.push_back(4);
    d.push_front(0);
    d.emplace_back(5);
    d.emplace_front(-1);
    d.pop_back();
    d.pop_front();
    cout<<d.front()<<" "<<d.back()<<endl;
    for(int val:d){
        cout<<val<<" ";
    }
    cout<<endl;
    cout<<d.size()<<endl;
    d.erase(d.begin()+2);
    d.insert(d.begin()+1,10);
    cout<<d.empty();

    d.clear();




    return 0;
}
