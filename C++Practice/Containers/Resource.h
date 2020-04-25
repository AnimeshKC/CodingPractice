#pragma once
#include <string>

class Resource {
private:
	std::string name;
public:
	Resource(std::string n);
	Resource(const Resource& r);
	Resource& operator=(const Resource& r);
	~Resource();
	std::string getName() const{ return name; }
};
