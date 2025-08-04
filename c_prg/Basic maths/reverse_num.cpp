#include<bits/stdc++.h>
using namespace std;
int rev_num(int n){
    int rev_no=0;
    while(n>0)
{
    int ld=n%10;
    rev_no=rev_no*10+ld;
    n=n/10;
}
return rev_no;
}
int main(){
    int n;
    cout<<"Enter number you want to reverse: ";
    cin>>n;
    cout<<"The number " <<n<<" after reversing is "<<rev_num(n);
    return 0;
}