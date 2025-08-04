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
    cout<<"Enter number you want to check for Palindrome: ";
    cin>>n;
    bool palin=false;
    if(n==rev_num(n)){
        palin=true;
        cout<<"Yes it is a Palindrome. ";
    }
    else{
        cout<<"The number is not a Palindrome. ";
    }
    return 0;
}