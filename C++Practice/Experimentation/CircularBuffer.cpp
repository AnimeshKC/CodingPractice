#include <iostream>
#include <array>
#include <stdexcept>

template <typename T, int cap, typename Container = std::array<T, cap>>
class CircularBuffer {
public:
	CircularBuffer() : m_head_idx(0), m_tail_idx(0), m_size(0), m_capacity(cap), m_current(0) {};

	T& head() {
		return m_cont.at(m_head_idx);
	}
	T& tail() {
		return m_cont.at(m_tail_idx);
	}

	T const& head() const {
		return m_cont.at(m_head_idx);
	}
	T const& tail() const {
		return m_cont.at(m_tail_idx);
	}
	void push_back() noexcept;
	void place_back();
	void pop();
	size_t size() const noexcept;
	size_t capacity() const noexcept;
	bool empty() const noexcept;
	bool full() const noexcept;
private:
	Container m_cont;
	int m_head_idx;
	int m_tail_idx;
	int m_size;
	int m_capacity;
	int m_current;
};
