#include<iostream>
using namespace std;
class A{
    public:
    void display(int a)
    {
        cout<<a<<endl;
    }
    void display(int a,int b)
    {
        cout<<a<<"\t"<<b<<endl;
    }
    void display(float a)
    {
        cout<<a<<endl;
    }


};
int main(){
    A a;
    a.display(10);
    a.display(4.5f);
    a.display(3,5);


    return 0;
}