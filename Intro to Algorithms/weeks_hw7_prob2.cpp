#include <iostream>
#include <cmath>
using namespace std;

double trackMyMoney(double money, double intRate, double taxRate, int years){

double firstmoney = money;
double finalMoney = 0;

	for(int i=1; i<years*12; i++){
		money = money*(1+intRate/12.0);
		if(i%12==0){
			money = money-(money-firstmoney)*taxRate;
			firstmoney = money;
		}	 
	}

return money;
}

int main(){

double m;
double i;
double t;
int y;

cout << "initial amount?" << endl;
cin >> m;
cout << "interest rate?" << endl;
cin >> i;
cout << "tax rate?" << endl;
cin >> t;
cout << "years?" << endl;
cin >> y;

double result = trackMyMoney(m, i, t, y);

cout << result << endl;

return 0;
}			 