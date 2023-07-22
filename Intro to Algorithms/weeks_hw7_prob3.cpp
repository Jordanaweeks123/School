#include <iostream>
using namespace std;

int factorial(int n, int k){

	if(n == 0 or n == k or k == 0){
	return 1;
	}else{
		return (factorial(n-1, k-1) + factorial(n-1, k));
	}
}
int algorithm(int n, int k){

int nFac = 1;
int kFac = 1;
int d = n-k;
int dFac = 1;

	if(n == 0 or n == k or k == 0){
	return 1;
	}
	for(int i=1; i<=n; i++){
		nFac *= i;
	}
	for(int i=1; i<=k; i++){
		kFac *= i;
	}
	for(int i=1; i<=d; i++){
		dFac *= i;
	}
return nFac/(kFac*dFac);
}

int main (){

int n;
int k;
int m;
int j;

cout << "n?" << endl;
cin >> n;
cout << "k?" << endl;
cin >> k;

m = factorial(n, k);
j = algorithm(n, k);

cout << "recursive method: " << m << endl;
cout << "non-recursive method: " << j << endl;

return 0;
}