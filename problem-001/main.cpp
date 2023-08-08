#include <iostream>

using namespace std;

int main(){
	int N = 1000;
	int sum = 0;

	for (int i=0; i<N; i++){
		if (i % 3 == 0 || i % 5 == 0)
		{
			sum += i;
		}
	}

	cout << "Sum of multiples of 3 or 5 below " << N << " is " << sum << endl;
	return 0;
}
