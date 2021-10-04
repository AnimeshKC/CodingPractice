#include "assert.h"
#include <string>
#include <iostream>
#include <iterator>
#include <cstddef>

template <typename Vector>
class SimpleVectorIterator {
	using value_type = typename Vector::ValueType;
	using iterator_category = std::forward_iterator_tag;
	using difference_type = std::ptrdiff_t;
	using pointer = value_type*;
	using reference = value_type&;

private:
	value_type* m_ptr;
public:
	SimpleVectorIterator(value_type* ptr): m_ptr(ptr) {}

	SimpleVectorIterator& operator++() {
		m_ptr++;
		return *this;
	}
	SimpleVectorIterator operator++(int) {
		//make a copy of the current iterator to return and then increment
		SimpleVectorIterator iterator = *this;
		++(*this);
		return iterator;
	}
	//This will be a forward iterator so it will not need decrementing

	//SimpleVectorIterator& operator--() {
	//	m_ptr--;
	//	return *this;
	//}
	//SimpleVectorIterator operator--(int) {
	//	SimpleVectorIterator iterator = *this;
	//	--(*this);
	//	return iterator;
	//}
	value_type& operator[](int index) {
		return *(m_ptr + index);
	}
	value_type* operator->() {
		return m_ptr;
	}
	value_type& operator*() {
		return *m_ptr;
	}
	bool operator==(const SimpleVectorIterator& other) const {
		return m_ptr == other.m_ptr;
	}
	bool operator!=(const SimpleVectorIterator& other) const {
		return !(m_ptr == other.m_ptr);
	}

};
template <typename Vector>
class SimpleVectorConstIterator {
	using value_type = typename Vector::ValueType;
	using iterator_category = std::forward_iterator_tag;
	using difference_type = std::ptrdiff_t;
	using pointer = value_type*;
	using reference = value_type&;

private:
	value_type* m_ptr;
public:
	SimpleVectorConstIterator(value_type* ptr) : m_ptr(ptr) {}

	SimpleVectorConstIterator& operator++() {
		m_ptr++;
		return *this;
	}
	SimpleVectorConstIterator operator++(int) {
		//make a copy of the current iterator to return and then increment
		SimpleVectorConstIterator iterator = *this;
		++(*this);
		return iterator;
	}
	//This will be a forward iterator so it will not need decrementing

	//SimpleVectorConstIterator& operator--() {
	//	m_ptr--;
	//	return *this;
	//}
	//SimpleVectorConstIterator operator--(int) {
	//	SimpleVectorIterator iterator = *this;
	//	--(*this);
	//	return iterator;
	//}
	value_type& operator[](int index) {
		return *(m_ptr + index);
	}
	value_type* operator->() const {
		return m_ptr;
	}
	value_type& operator*() const {
		return *m_ptr;
	}
	bool operator==(const SimpleVectorConstIterator& other) const {
		return m_ptr == other.m_ptr;
	}
	bool operator!=(const SimpleVectorConstIterator& other) const {
		return !(m_ptr == other.m_ptr);
	}

};
template <typename T>
class SimpleVector {
public:
	using ValueType = T;
	using Iterator = SimpleVectorIterator<SimpleVector<T>>;
	using ConstIterator = SimpleVectorConstIterator<SimpleVector<T>>;
private:
	size_t m_size = 0;
	size_t m_capacity = 0;
	T* m_data = nullptr;
	//assumption: realloc is only used to grow the size, not to strip elements and shink the size
	void realloc(size_t new_capacity) {
		if (new_capacity <= m_capacity) return;
		T* new_block = (T*)::operator new (new_capacity * sizeof(T));
		for (size_t i = 0; i < m_size; i++) {
			new (&new_block[i]) T(std::move(m_data[i]));
		}
		for (size_t i = 0; i < m_size; i++) {
			//call the type's destructor
			m_data[i].~T();
		}
		::operator delete(m_data, m_capacity * sizeof(T));

		m_data = new_block;
		m_capacity = new_capacity;
	}

public:
	SimpleVector() {
		this->realloc(2);
	}
	~SimpleVector() {
		clear();
		::operator delete(m_data, m_capacity * sizeof(T));
	}
	void push_back(const T& val) {
		//if the vector is full, need to allocate more memory
		if (m_size == m_capacity) {
			this->realloc(m_capacity + m_capacity / 2);
		}
		new (&m_data[m_size++]) T(val);
	}
	size_t size() const {
		return m_size;
	}
	void push_back(const T&& val) {
		if (m_size == m_capacity) {
			this->realloc(m_capacity + m_capacity / 2);
		}

		new (&m_data[m_size++]) T(std::move(val)); //-V1030
	}
	void pop_back() {
		if (m_size > 0) {
			m_size--;
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
		//placement new operator
		new (&m_data[m_size++]) T(std::forward<Args>(args)...);
	}
	const T& operator[](size_t index) const {
		assert(index < m_size);
		return m_data[index];
	}
	T& operator[](size_t index) {
		assert(index < m_size);
		return m_data[index];
	}
	Iterator begin() {
		return Iterator(m_data);
	}
	Iterator end() {
		return Iterator(m_data + m_size);
	}
	ConstIterator begin() const {
		return ConstIterator(m_data);
	}
	ConstIterator end() const {
		return ConstIterator(m_data + m_size);
	}
};

template <typename T>
void printSimpleVec(const SimpleVector<T>& vec) {
	for (const auto& value : vec) {
		std::cout << value << "\n";
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

	std::cout << "Trying int vector \n";

	SimpleVector<int> vec2;
	vec2.push_back(15);
	int i1 = 20;
	vec2.push_back(i1);
	vec2.emplace_back(55);

	std::cout << "Vector print Before popping: \n";
	printSimpleVec(vec2);


	std::cout << "\n Vector print After popping one: \n";
	vec2.pop_back();
	printSimpleVec(vec2);

	std::cout << "\n Vector print After clearing: \n";
	vec2.clear();
	printSimpleVec(vec2);

	std::cout << "done";
}