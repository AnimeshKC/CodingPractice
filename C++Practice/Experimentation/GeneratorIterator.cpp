#include <iterator>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>


template <typename T = long>
class PrimeGeneratorIterator {
private:
	T currentPrime;
public:
	using iterator_category = std::input_iterator_tag;
	using value_type = T;
	using difference_type = T;
	using pointer = T*;
	using reference = T&;

	bool operator==(const PrimeGeneratorIterator& Other) {
		return this->currentPrime == Other.currentPrime;
	}
	bool operator!=(const PrimeGeneratorIterator& Other) {
		return this->currentPrime != Other.currentPrime;
	}
	reference operator*() {
		return currentPrime;
	}
	pointer operator->() {
		return &currentPrime;
	}

	PrimeGeneratorIterator& operator++() {
		generateNextPrime();
		return *this;
	}
	PrimeGeneratorIterator operator++(int) {
		PrimeGeneratorIterator pgi(*this);
		generateNextPrime();
		return pgi;
	}

	void generateNextPrime() {
		while (!isPrime(++currentPrime)){}
	}
	bool isPrime(T val) {
		if (val <= 1) {
			return false;
		}
		else if (val == 2) {
			return true;
		}
		else if (val % 2 == 0) {
			return false;
		}
		for (int i = 3; i <= std::sqrt(val); i++) {
			if (val % i == 0) {
				return false;
			}
		}
		return true;
	}

	PrimeGeneratorIterator() : currentPrime(2) {}
	PrimeGeneratorIterator(T initialValue) : currentPrime(initialValue) {
		if (!isPrime(currentPrime)) {
			generateNextPrime();
		}
	}


};

//void GeneratorIteratorDriver() {
//	PrimeGeneratorIterator<> start;
//	PrimeGeneratorIterator<> end(1000);
//	std::copy(start, end, std::ostream_iterator<long>(std::cout, " "));
//	std::cout << "\n";
//}