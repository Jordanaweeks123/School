#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
double word;
double bigNum;
bigNum = 0;
double sum;
int i;
i = 0;
ifstream fin;
fin.open("dat_hw4_prob4.txt");
if (fin.is_open()) {
	while (fin >> word) {
	cout << word << endl;
	if (word > bigNum){
	bigNum = word;
	}
	sum += word;
	word++;
	i++;	
}
}	
	cout << "Number of numbers: " << i << endl;
	cout << "Sum of numbers: "<<sum<<endl;
	cout <<"Average: "<<sum/i<<endl;
	cout <<"Largest number: "<<bigNum<<endl;
return 0;
} 
