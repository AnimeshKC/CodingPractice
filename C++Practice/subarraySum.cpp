#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

int subarraySum(const vector<int>& nums, const int k) {
	int answer = 0;
	int sum = 0;
	unordered_map<int, int> hash;
	hash[0]++;
	for (int R : nums) {
		sum += R;
		answer += hash[sum - k];
		hash[sum]++;
	}
	return answer;
}
