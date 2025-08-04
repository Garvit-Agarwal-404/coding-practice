#include<bits/stdc++.h>
using namespace std;
int count_dig(int n){ // to count number of digits
    int count=(int)(log10(n)+1);
    return count;
}
int int_pow(int base, int exp) { // to calculate power
    int result = 1;
    while (exp--) {
        result *= base;
    }
    return result;
}
void armstrong(int n){
    int temp=n;
    bool arms=false;
    int dig=count_dig(n);
    
    int sum=0;
    while(n>0){
        int ld=n%10;
        sum=sum+int_pow(ld,dig);
        n=n/10;
    }
    if(sum==temp){
        arms=true;
        cout<<"The number is an armstrong. ";
    }
    else{
        cout<<"The number is not an armstrong. ";
    }
}
int main(){
    int n;
    cout<<"Enter the number you want to check armstrong or not: ";
    cin>>n;
    armstrong(n);

    return 0;
}