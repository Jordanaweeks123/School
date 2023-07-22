#include <iostream>
#include <fstream>
using namespace std;

int main(){

ofstream myfile;

myfile.open("MultiplicationTable.txt");

int i;
int d;

for (i=1; i<=9; i++){
   for (d=1; d<=i; d++){
	cout<<i*d<<" ";
	if (d==i){
	cout<<endl;
	}
	}
}

myfile.close();

return 0;
}
	