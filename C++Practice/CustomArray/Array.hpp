#pragma once

#include <cassert>
#include <ostream>
#include <utility>

//Array implementation inspired by Giovanni Dicanio's Introduction to Data Structures in C++ course
//minor changes such as the use of size_t

class IndexOutOfBoundsException {};

template <typename T>
class Array {
private:
	T* m_ptr{ nullptr };
	size_t m_size{ 0 };
	bool IsValidIndex(int index) const {
		return (index >= 0) && (index < m_size);
	}

public:
	Array() = default; //default constructor

	explicit Array(size_t size) {
		if (size != 0) {
			m_ptr = new T[size]{};
			m_size = size;
		}
	}
	bool IsEmpty() const {
		return (m_size == 0);
	}
	size_t Size() const {
		return m_size;
	}
	friend void swap(Array& a, Array& b) noexcept {
		std::swap(a.m_ptr, b.m_ptr);
		std::swap(a.m_size, b.m_size);
	}
	Array(const Array& source) { //copy constructor
		if (!source.IsEmpty()) {
			m_size = source.m_size;
			m_ptr = new T[m_size]{};
			for (int i = 0; i < m_size; i++) {
				m_ptr[i] = source.m_ptr[i];
			}
		}
	}
	Array(Array&& source): //move constructor
		m_ptr{ source.m_ptr }, m_size{ source.m_size }{
		//remove the source that is being moved
		source.m_ptr = nullptr;
		source.m_size = 0;
	}
	~Array() {
		delete[] m_ptr; //free up entire array
	}
	Array& operator=(Array source) {
		swap(*this, source);
		return *this;
	}
	// Safe element access with bounds checking
	T& operator[](int index) {
		if (!IsValidIndex(index)) {
			throw IndexOutOfBoundsException{};
		}

		return m_ptr[index];
	}

	// Safe read-only element access with bounds checking
	T operator[](int index) const {
		if (!IsValidIndex(index)) {
			throw IndexOutOfBoundsException{};
		}

		return m_ptr[index];
	}
};
