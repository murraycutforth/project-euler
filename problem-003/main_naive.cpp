#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;


bool is_prime(long x)
{
	for (long i=2; i<=x/2; i++)
	{
		if (x % i == 0)
		{
			return false;
		}
	}
	return true;
}


class CachedPrimes
{
	unordered_map<int, bool> number_to_prime;

	public:

	bool is_prime_cached(int x)
	{
		if (number_to_prime.count(x) > 0)
		{
			return number_to_prime[x];
		}
		else
		{
			bool val = is_prime(x);
			number_to_prime.emplace(x, val);
			return val;
		}
	}
};




void find_factors(long x, vector<long>& factors, CachedPrimes& cp)
{
	if (is_prime(x))
	{
		factors.push_back(x);
		return;
	}
	else
	{
		for (long i=2; i<=x/2; i++)
		{
			if (x % i == 0 && cp.is_prime_cached(i))
			{
				factors.push_back(i);
				find_factors(x / i, factors, cp);
				return;
			}
		}
	}
}


int main()
{
	vector<long> factors;
	CachedPrimes cp;
	find_factors(600851475143, factors, cp);
	cout << *max_element(factors.begin(), factors.end()) << endl;

	return 0;
}
