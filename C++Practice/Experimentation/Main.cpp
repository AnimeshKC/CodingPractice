#include "CircularBuffer.hpp"
void strCopyingExperimentation();
void testLambda();
void topologicalSortDriver();
void simpleVectorDriver();
void SpecializedIsGreaterDriver();
void AlwaysExceptionDriver();

#include <iostream>
int main() {
	CircularBuffer<int, 10> cbuff;
	cbuff.push_back(10);
	std::cout << cbuff.size() << " " << cbuff.capacity() << "\n";

}
