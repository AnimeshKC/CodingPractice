#include <iostream>
template <typename T, typename V>
void SpecializedIsGreater(T x1, V x2) {
	bool res = x1 > x2;

	std::cout << "General comparison result: " << res << "\n";
}

template <>
void SpecializedIsGreater(int x1, int x2) {
	bool res = x1 > x2;
	std::cout << "Integer comparison result: " << res << "\n";
}

void SpecializedIsGreaterDriver() {
	std::cout << std::boolalpha;
	SpecializedIsGreater(7.5, 4);
	SpecializedIsGreater(3, 4);
}