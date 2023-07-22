#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() 
{ 
	int num = 0;
	int numMax;
	cout << "How many random points?" << endl;
	cin >> numMax; 
	double x, y;  
	double pi; 
 	int circle = 0; 
	int square = 0;
	srand(time(NULL)); 
for (num = 0; num < numMax; num++) { 
	x = double(rand()%(numMax+1))/double(numMax); 
	y = double(rand()%(numMax+1))/double(numMax); 
if (x*x+y*y<= 1){ 
	circle++; 
}
	square++; 
}      
pi = double(4*circle)/square; 
cout << "Pi = " << pi;  
return 0; 
} 