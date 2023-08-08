#include <iostream>
#include <vector>

using namespace std;


vector<int> fib(int max_val = 4000000){
	vector<int> terms = {1, 2};

	int next_val = 3;

	while (next_val <= max_val){
		terms.push_back(next_val);
		next_val = terms[terms.size() - 2] + terms.back();
	}

	return terms;
}


int main(){
	vector<int> terms (fib());

	int result = 0;

	for (int i=1; i<terms.size(); i+=3){
		result += terms[i];
	}

	cout << result;
}



