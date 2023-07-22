#include <iostream>
using namespace std;

int main () {

double a;

int b;

double i;

cin >> a;

b = a+1;

i = a;

bool c;

c = (a+0.5 > b);

bool d;

d = (a+0.5 < b);

bool g;

g = !(int(a+0.5)%2 == 0);

bool h;

h = (int(a+0.5)%2 == 0);

if (c) {

	cout << int(a+0.5) << endl;

} else if (d) {

	cout << int(a) << endl;
}

else if (h) {

	cout << i+0.5 << endl;

} else if (g) {

	cout << i-0.5 << endl;
}

return 0;

}