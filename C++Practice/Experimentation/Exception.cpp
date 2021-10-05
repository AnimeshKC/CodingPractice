#include <iostream>
#include <exception>

class CustomException : public std::exception {
	std::string m_message;
public:
	CustomException(std::string message): m_message(message){}
	const char* what() const noexcept override{
		return m_message.c_str();
	}
};

class AlwaysException {
public:
	AlwaysException() {
		throw CustomException("Internal Error Occured");
	}
};

void AlwaysExceptionDriver() {
	try {
		AlwaysException a;
	}
	catch (std::exception& except) {
		std::cout << except.what();
	}
}