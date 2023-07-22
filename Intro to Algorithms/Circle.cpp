#include <iostream>
#include <string>
using namespace std;

int main() {

double r;
double x0;
double y0;
double x1;
double y1;

cout << "r?" << endl;
cin >> r;
cout << "x0?" << endl;
cin >> x0;
cout << "y0?" << endl;
cin >> y0;
cout << "x1?" << endl;
cin >> x1;
cout << "y1?" << endl;
cin >> y1;

bool a;
bool b;

a = (y1-y0 > r);
b = (x1-y0 > r);

if (a) {

	cout << "The point is outside the circle." << endl;

}

if (b) {

	cout << "The point is outside the circle." << endl;

}

bool c;
bool d;

c = (y1-y0 <= r);
d = (x1-x0 <= r);

if (c and d) {

	cout << "The point is within the circle." << endl;

}

return 0;

}