#include <iostream>
#include <vector>
#include <numeric>


using namespace std;

void multiply(std::vector<int>& num, int factor)
{
	int rem = 0;

	for (int i=0; i<num.size(); i++)
	{
		int x = num[i] * factor + rem;
		num[i] = x % 10;
		rem = x / 10;
	}

	if (rem > 0)
	{
		num.push_back(rem);
	}
}



int main()
{
	std::vector<int> num (1, 1);
	int exponent = 1000;
	int base = 2;

	for (int i=0; i<exponent; i++)
	{
		multiply(num, base);
	}

	int result = accumulate(num.begin(), num.end(), 0);

	cout << result << endl;
}
