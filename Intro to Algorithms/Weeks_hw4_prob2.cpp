#include <iostream>
using namespace std;

int main (){
int myNum;
cin >> myNum;
while(!(myNum%2==0)){
	cin >> myNum;
	}
while(myNum<=0){
	cin >> myNum;
	}
if(myNum>0 and myNum%2==0){
cout<<"Positive and Even"<<endl;
	}
return 0;
}
