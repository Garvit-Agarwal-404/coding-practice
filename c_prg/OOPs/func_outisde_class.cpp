#include<bits/stdc++.h>
using namespace std;
class A{
    int a,b,sum;
    public:
     int sum_of(int a,int b);
     void display();


};

int A::sum_of(int n,int m){
    sum=n+m;
    return sum;
}
void A::display(){
    cout<<"The sum is"<<sum;
}
int main()
{
    A a;
    a.sum_of(2,8);
    a.display();
    return 0;
}
