#include <iostream>
using namespace std;
int main () {
double w;
double l;
cout << "Width? " << endl;
cin >> w;
cout << "Length? " << endl;
cin >> l;
cout << "Width=" << w << endl;
cout << "Length=" << l << endl;
cout << "Area=" << w*l << endl;
cout << "Perimeter=" << (w+l)*2 << endl;
return 0;
}