#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>

int main() {

	std::ofstream writeToFile;
	std::ifstream readFromFile;
	std::string txtToWrite = "";
	std::string txtFromFile = "";
	writeToFile.open("test.txt", std::ios_base::out | std::ios_base::trunc);
	if (writeToFile.is_open()) {
		writeToFile << "Beginning of File\n";

	}
	return 0;
}