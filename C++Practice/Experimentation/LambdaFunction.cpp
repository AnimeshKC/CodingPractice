#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


void testLambda() {
	std::vector<int> v = { 15, 26, 18 };
	std::vector<int> q;
	constexpr int val_filter = 17;
	std::copy_if(v.begin(), v.end(), std::back_inserter(q), [val_filter](int val) {
		return val > val_filter;
		});
	std::cout << "Let's check the filter of " << val_filter << "\n";
	for (int val : q) {
		std::cout << val << "\n";
	}
}