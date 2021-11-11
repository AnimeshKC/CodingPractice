#pragma once
#include <iostream>
#include <array>
#include <iterator>
#include <stdexcept>
#include <algorithm>

template <typename T, int cap, typename Container = std::array<T, cap>>
class CircularBuffer {
public:
	CircularBuffer() : m_head(0), m_tail(0), m_size(0), m_capacity(cap), m_current(0){};

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
	template <typename Buffer, typename Iterator>
	class CircularBufferIterator {
	public:
		using iterator_category = std::forward_iterator_tag;
		using value_type = typename Buffer::value_type;
		using difference_ptr = std::ptrdiff_t;
		using pointer = typename Buffer::value_type*;
		using reference = typename Buffer::value_type&;

		CircularBufferIterator() : _done(true) {};
		CircularBufferIterator(const Buffer& buf, Iterator begin) : _buf(buf), _begin(begin), _cursor(begin), _done(false) {}
		CircularBufferIterator(const Buffer& buf, Iterator begin, bool done) : _buf(buf), _begin(begin), _cursor(begin), _done(done) {}

		reference operator*() const {
			return *_cursor;
		}
		pointer operator->() const {
			return _cursor;
		}
		CircularBufferIterator& operator++() {
			++_cursor;
			if (_cursor == _buf.end()) {
				_cursor = const_cast<Iterator>(_buf.begin());
			}
			_done = _cursor == _begin;

			return *this;
		}
		CircularBufferIterator operator++(int) {
			iterator temp = *this;
			++_cursor;
			if (_cursor == _buf.end()) {
				_cursor = const_cast<Iterator>(_buf.begin());
			}
			_done = _cursor == _begin;

			return temp;
		}
		bool operator=(const CircularBufferIterator& it) const {
			if (_done && it._done) {
				return true;
			}
			else if (!_done && !it._done) {
				return (this->cursor == it->_cursor);
			}
			return false;
		}
		bool operator!=(const CircularBufferIterator& it) const {
			return !(*this == it);
		}
	private: 
		const Buffer& _buf;
		const Iterator _begin;
		Iterator _cursor;
		bool _done;
	};
	typedef CircularBufferIterator<Container, typename Container::iterator> iterator;
	using value_type = iterator::value_type;
	iterator begin() {
		unsigned int offset = m_head % m_capacity;
		return CircularBuffer::iterator(m_container, m_container.begin() + offset);
	}
	iterator end() {
		unsigned int offset = m_tail + 1  % m_capacity;
		return CircularBuffer::iterator(m_container, m_container.begin() + offset, full);
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

void CircularBufferIteratorDriver() {
	CircularBuffer<int, 7> buffer;
	std::cout << "Buffer Size: " << buffer.size() << "\n";

	//auto bufInsert = std::back_insert_iterator<CircularBuffer<int, 7>>(buffer);

	for (int i = 0; i < 17; i++) {
		buffer.push_back(i*10);
	}
	std::cout << "Buffer Size: " << buffer.size() << "\n";
	std::copy(std::begin(buffer), std::end(buffer), std::ostream_iterator<int>(std::cout, " "));
	std::cout << "\n";

	while (!buffer.empty()) {
		std::cout << "popping head: " << buffer.head() << "/n";
		buffer.pop();
	}
}