#include <string>
#include <iostream>
#include <map>
#include <fstream>
#include <sstream>
#include <utility>

using std::string, std::pair;

//using std::multimap, std::ifstream, std::istringstream
void wordListing(string fileName) {
	std::ifstream in(fileName);
	using mapType = std::multimap<string, pair<int, int>>;
	mapType wordPositions;

	int lineNumber = 0, wordInLine = 0;
	string line = "";

	//read each line of file
	while (std::getline(in, line)) {
		lineNumber++;
		std::getline(in, line);
		std::stringstream iss(line);
		string word = "";

		//read each word of file
		while (iss >> word) {
			wordInLine++;
			word.erase(std::remove_if(word.begin(), word.end(), &std::ispunct));
			wordPositions.insert(std::make_pair(word, std::make_pair(lineNumber, wordInLine)));
		}
		wordInLine = 0;
	}

	//print the words
	mapType::const_iterator it = wordPositions.cbegin();
	mapType::const_iterator it2 = it;

	for (it; it != wordPositions.cend(); it = it2) {
		int frequency = wordPositions.count(it->first);
		std::cout << "The word " << it->first << " appears " << frequency << " times in the following:" << "\n";
		for (; it2 != wordPositions.cend() && it2->first == it->first; it2++) {
			auto [line, word] = it2->second;
			std::cout << "\t Line number: " << line << "; word position: " << word << "\n";
		}
	}
	in.close();
}

void wordListingDriver() {
	wordListing("shakespeare.txt");
}