#include <iostream>
#include <string>
class Printable {
public:
	virtual std::string GetClassName() const = 0;
};


class Entity : public Printable {
	float x;
	float y;
public:
	Entity() {
		x = 0.0f;
		y = 0.0f;
	}
	Entity(float x) {
		this->x = x;
		y = 0.0f;
	}
	Entity(float x, float y) {
		this->x = x;
		this->y = y;
	}
	void Print() const {
		std::cout << "x value is " << this->x << ", y value is " << this->y << "\n";
	}
	std::string GetClassName() const {
		return "Entity";
	}
};
void printClass(const Printable& p) {
	std::cout << p.GetClassName();
}
void printClassPointer(const Printable* const p) {
	std::cout << p->GetClassName();
}