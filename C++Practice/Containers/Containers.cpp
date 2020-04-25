#include <vector>
#include <iostream>
#include <stdexcept>
#include "Resource.h"

using std::vector;
using std::cout;

int main() {
	vector<int> numbers;
	numbers.insert(numbers.end(), { 1, 5, 6 });
	numbers.push_back(6);
	numbers[2] = 7;

	for (int i : numbers) {
		cout << i << "\n";
	}
	
	//Resource r("local");
	{
		cout << "-- \n";
		vector<Resource> resources;
		resources.reserve(2);
		resources.emplace_back("local");
		cout << "-- \n";
		resources.emplace_back(("first"));
		cout << "--\n";

	}
	return 0;
}