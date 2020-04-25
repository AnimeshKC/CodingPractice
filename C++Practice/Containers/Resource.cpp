#include "Resource.h"
#include <iostream>

using std::cout;
using std::string;

Resource::Resource(string n) : name(n) {
	cout << "constructing " << name << "\n";
}
Resource::Resource(const Resource& r) : name(r.name) {
	cout << "copy constructing " << name << "\n";
}
Resource::~Resource() { cout << "Destructing \n"; }

Resource& Resource::operator=(const Resource& r) {
	name = r.getName();
	cout << "copy assigning" << name << "\n";
	return *this;
}