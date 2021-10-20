#include <iostream>
#include <numeric>
#include <vector>
#include <iterator>

using std::vector;
void OutputIteratorDriver() {
	std::istream_iterator<double> end;
	//use standard input as the input stream
	std::istream_iterator<double> din(std::cin);

	vector<double> doubles;
	std::back_insert_iterator<vector<double>> bins(doubles);

	while (din != end) {
		*bins++ = *din++;
	}
	std::partial_sum(doubles.begin(), doubles.end(), std::ostream_iterator<double>(std::cout, " "));
	std::cout << "\n";
}