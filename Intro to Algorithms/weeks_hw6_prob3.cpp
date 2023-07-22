#include <iostream>
using namespace std;
int countRabbit(int nRabbits, int nYears)
{
	

	for(int i=0; i<=nYears; i++){
	nRabbits=int(nRabbits*0.95)+5;
	}

	return nRabbits;
}

int main(){
    cout << countRabbit(15,50)<<endl;
    return 0;

}