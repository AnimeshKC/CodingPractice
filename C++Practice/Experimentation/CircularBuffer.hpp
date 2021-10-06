#pragma once
#include <iostream>
#include <array>
#include <stdexcept>

template <typename T, int cap, typename Container = std::array<T, cap>>
class CircularBuffer {
public:
	CircularBuffer() : m_head(0), m_tail(0), m_size(0), m_capacity(cap), m_current(0) {};

	T& head() {
		return m_container.at(m_head);
	}
	T& tail() {
		return m_container.at(m_tail);
	}

	T const& head() const {
		return m_container.at(m_head);
	}
	T const& tail() const {
		return m_container.at(m_tail);
	}
	void push_back(T val) noexcept {
		if (m_current >= m_capacity) {
			m_current = 0;
		}
		m_container[m_current++] = val;
		m_tail = m_current - 1;

		if (m_size++ >= m_capacity) {
			m_size = m_capacity;
			incrementHead();
		}
	}
	
	void pop() {
		if (empty()) {
			throw std::underflow_error("pop(): cannot pop empty container");
		}
		incrementHead();
		m_size--;
	}
	size_t size() const noexcept { return m_size; }
	size_t capacity() const noexcept { return m_capacity; }
	bool empty() const noexcept {
		if (m_size <= 0) {
			return true;
		}
		else {
			return false;
		}
	}
	bool full() const noexcept {
		if (m_size >= m_capacity) {
			return true;
		}
		else {
			return false;
		}
	}
	void place_back(T val) {
		if (full()) {
			throw std::overflow_error("place_back(): full buffer");
		}
		push_back(val);
	}
private:
	Container m_container;
	int m_head;
	int m_tail;
	int m_size;
	int m_capacity;
	int m_current;
private:
	void incrementHead() {
		m_head++;
		if (m_head >= m_capacity) {
			m_head = 0;
		}
	}
};

void CircularBufferDriver() {
	CircularBuffer<int, 10> cbuff;
	for (int i = 0; i < 13; i++) {
		cbuff.push_back(i);
	}
	while (!cbuff.empty()) {
		std::cout << "popping index: " << cbuff.head() << "\n";
		cbuff.pop();
	}
}