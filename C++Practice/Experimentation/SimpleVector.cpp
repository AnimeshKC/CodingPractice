#include "assert.h";

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
			new_block[i] = m_data[i];
		}
		delete[] m_data;
		m_data = new_block;
		m_capacity = new_capacity;
	}
public:
	SimpleVector() {
		realloc(2);
	}
	void push_back(T val) {
		//if the vector is full, need to allocate more memory
		if (m_size == m_capacity) {
			realloc(m_capacity + m_capacity / 2);
		}
		m_data[m_size++] = val;
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