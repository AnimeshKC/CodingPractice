#include <iostream>
#include <string>

class SimpleString {
private:
	char* m_buffer;
	unsigned int m_size;
public:
	SimpleString(const char* str) {
		m_size = strlen(str);
		m_buffer = new char[m_size + 1];
		memcpy(m_buffer, str, m_size);

		//ensure null-terminated
		m_buffer[m_size] = 0;
	}
	SimpleString(const SimpleString& other) : m_size(other.m_size) {
		m_buffer = new char[m_size + 1];
		memcpy(m_buffer, other.m_buffer, m_size + 1);
	}
	SimpleString& operator=(const SimpleString& other) {
		if (this == &other) {
			return *this;
		}
		m_size = other.m_size;
		delete m_buffer;
		m_buffer = new char[m_size + 1];
		memcpy(m_buffer, other.m_buffer, m_size + 1);
		return *this;
	}
	~SimpleString() {
		delete m_buffer;
	}
	char& operator[](unsigned int i) {
		return m_buffer[i];
	}
	int getSize() {
		return m_size;
	}
	//enable the function to access the private variable
	friend std::ostream& operator<<(std::ostream& stream, const SimpleString& str);

};
//operator overload so that cout can use this class
std::ostream& operator<<(std::ostream& stream, const SimpleString& str) {
	stream << str.m_buffer;
	return stream;
}
//Make sure this function takes const reference so that the parameter doesn't copy the object
void printSimpleString(const SimpleString& str) {
	std::cout << str;
}
void strCopyingExperimentation() {
	SimpleString s1 = "ContentsS1";
	SimpleString s2 = s1;
	int s_size = s1.getSize();
	s2[s_size - 1] = '2';
	std::cout << "s1 is " << s1 << ", and s2 is " << s2 << "\n";

	//Now try copy assignment
	s2 = s1;
	std::cout << "s1 is " << s1 << ", and s2 is " << s2 << "\n";
}