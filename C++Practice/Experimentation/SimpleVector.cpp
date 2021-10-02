#include "assert.h"
#include <string>
#include <iostream>
template <typename T>
class SimpleVector {
private:
	size_t m_size = 0;
	size_t m_capacity = 0;
	T* m_data = nullptr;
	//assumption: realloc is only used to grow the size, not to strip elements and shink the size
	void realloc(size_t new_capacity) {
		if (new_capacity <= m_capacity) return;
		T* new_block = new T[new_capacity];
		for (size_t i = 0; i < m_size; i++) {
			//move if possible
			new_block[i] = std::move(m_data[i]);
		}
		delete[] m_data;
		m_data = new_block;
		m_capacity = new_capacity;
	}

public:
	SimpleVector() {
		this->realloc(2);
	}
	~SimpleVector() {
		delete[] m_data;
	}
	void push_back(const T& val) {
		//if the vector is full, need to allocate more memory
		if (m_size == m_capacity) {
			this->realloc(m_capacity + m_capacity / 2);
		}
		m_data[m_size++] = val;
	}
	size_t size() const {
		return m_size;
	}
	void push_back(const T&& val) {
		if (m_size == m_capacity) {
			this->realloc(m_capacity + m_capacity / 2);
		}
		m_data[m_size++] = std::move(val);
	}
	void pop_back() {
		if (m_size > 0) {
			m_size--;
			//delete the memory in this location
			m_data[m_size].~T();
		}
	}
	void clear() {
		while (m_size > 0) {
			this->pop_back();
		}
	}
	//create the type within the class
	template <typename... Args>
	void emplace_back(Args&&... args) {
		if (m_size == m_capacity) {
			realloc(m_capacity + m_capacity / 2);
		}
		m_data[m_size++] = T(std::forward<Args>(args)...);
	}
	const T& operator[](size_t index) const {
		assert(index < m_size);
		return m_data[index];
	}
	T& operator[](size_t index) {
		assert(index < m_size);
		return m_data[index];
	}
};

template <typename T>
void printSimpleVec(const SimpleVector<T> &vec) {
	for (int i = 0; i < vec.size(); i++) {
		std::cout << vec[i] << "\n";
	}
}
void simpleVectorDriver() {
	SimpleVector<std::string> vec1;
	vec1.push_back("hello");
	std::string s1 = "This string";
	vec1.push_back(s1);
	vec1.emplace_back("another string");

	std::cout << "Vector print Before popping: \n";
	printSimpleVec(vec1);

	std::cout << "\n Vector print After popping one: \n";
	vec1.pop_back();
	printSimpleVec(vec1);

	std::cout << "\n Vector print After clearing: \n";
	vec1.clear();
	printSimpleVec(vec1);

	std::cout << "done";
}