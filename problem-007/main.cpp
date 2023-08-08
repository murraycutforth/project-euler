#include <iostream>
#include <cmath>


using namespace std;


bool is_prime(int x)
{
	int r = int(sqrt(x));

	for (int i=2; i<=r; i++){
		if (x % i == 0){
			return false;
		}
	}

	return true;
}


int main()
{
	int n = 2;
	int x = 3;

	while (n < 10001)
	{
		x += 2;

		if (is_prime(x))
		{
			n++;
		}
	}

	cout << x;
}

