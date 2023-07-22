#include <iostream>
using namespace std;

int main (){

 int year;

 bool isLeapYear;

 cin >> year;

 bool a;
 bool b;
 
a = ((year%100==0) and (year%400==0));
b = (!(year%100==0) and (year%4==0));
 
isLeapYear = a or b;

 if (isLeapYear){
 cout << year << " is a leap year." << endl;
 }else{
 cout << year << " is not a leap year." << endl;
 }
 return 0;
}
