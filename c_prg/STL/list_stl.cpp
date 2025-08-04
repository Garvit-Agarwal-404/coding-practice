#include<bits/stdc++.h>
#include<list>
using namespace std;
int main(){
    list<int>lst={1,2,3};
    // list is implemented as a doubly linked list so we can insert and delete both in front and back
    // and random acess is not allowed 
    lst.push_back(4);
    lst.push_front(0);
    lst.emplace_back(5);
    lst.emplace_front(-1);
    lst.pop_back();
    lst.pop_front();
    cout<<lst.size()<<endl;
    // to print the list
    for(auto  it=lst.begin();it!=lst.end();it++){ // auto keyword
        cout<<*(it)<<" ";
    }
    cout<<endl<<lst.front()<<" "<<lst.back();
    


    return 0;
}