#include <iostream>
#include<cmath>
#include <cstdlib>
using namespace std;

int reverseInteger(int n){

int result;
int result2;
int mySum=0;
int i=0;
do{
	i++;
}while(abs(n)/pow(10,i)>=1);
do{
	result = n%10;
	result2 = result * pow(10,i-1);
	i--; 
	n=n/10;
	mySum += result2;
}while(abs(n)>=1);
	
	return mySum;
}

int main(){

int n;

cin >> n;

int m=reverseInteger(n);

cout<<m<<endl;

return 0;
}