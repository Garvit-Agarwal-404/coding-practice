#include<bits/stdc++.h>
using namespace std;
int main()
{   
    vector<int>v;    // intitalising a vector 
    cout<<v.size()<<endl;  // to get size of vector
    v.push_back(1);  // to insert an element in the vector
    v.push_back(5);
    v.push_back(7);
    cout<<v.capacity()<<endl; // to get capacity of vector
    v.pop_back();    // to pop element form vector
    for(int val:v){       // to print a vector
        cout<<val<<" ";
    }
    vector<int>v1={1,2,3,4,5};
    vector<int>v2(v1);   // copying a vector into another vector
    cout<<"value of v1:";
    for(int val:v1){       // to print a vector
        cout<<val<<" ";
    }
    cout<<"Vale of v2:";
    for(int val:v2){       // to print a vector
        cout<<val<<" ";
    }
    cout<<"Value of v3";
    vector<int>v3(3,10);
    for(int val:v3){
        cout<<val<<" ";
    }
    cout<<endl<<"Value of v3: ";
    
    for(auto it=v3.begin();it!=v3.end();it++){
        cout<<*(it)<<" ";
    }
    return 0;
}