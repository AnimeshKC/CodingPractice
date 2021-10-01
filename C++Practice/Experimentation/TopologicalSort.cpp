#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <iostream>

using std::unordered_map, std::vector, std::unordered_set, std::cout;

bool intIsFoundInset(const unordered_set<int>& s, int val) {
	if (s.find(val) == s.end()) {
		return false;
	}
	else {
		return true;
	}
}

//if we don't have to worry about cycles, it can be a void instead of a boolean, and there will be no visiting set
bool dfs(int start, unordered_map<int, vector<int>>& graph, vector<int>& order, unordered_set<int>& visited, unordered_set<int>& visiting) {
	//if this value has already been visited, we can move on
	if (intIsFoundInset(visited, start)) return false;
	//if we were visting this value, this is a cycle
	if (intIsFoundInset(visiting, start)) return true;

	visiting.emplace(start);
	for (int& prereq : graph[start]) {
		bool containsCycle = dfs(prereq, graph, order, visited, visiting);
		if (containsCycle) return true;
	}
	visited.emplace(start);
	//erase from visiting as we are done with this value
	visiting.erase(start);
	order.push_back(start);
	return false;
}

vector<int> topologicalSort(vector<int> jobs, vector<vector<int>> deps) {
	unordered_map<int, vector<int>> graph;
	
	//example deps: { {1,2}, {1,3}, {3,2}, {4,2}, {4,3} }
	//example graph: {2: {1, 3, 4}, 3: {1,4}}
	for (const vector<int>& d : deps) {
		
		//use emplace to generate empty vector if d[1] is not yet a key in the hashmap
		vector<int> empty_vec = {};
		auto pair = graph.emplace(d[1], empty_vec);

		//add d[0] to d[1]'s dependency list
		(pair.first)->second.push_back(d[0]);
	}
	unordered_set<int> visited;
	unordered_set<int> visiting;
	vector<int> order;
	for (int& job : jobs) {
		bool containsCycle = dfs(job, graph, order, visited, visiting);
		if (containsCycle) return {};
	}
	return order;
}
void topologicalSortDriver() {
	vector<int> jobs1 = { 1,2,3,4 };
	vector<vector<int>> deps1 = { {1,2}, {1,3}, {3,2}, {4,2}, {4,3} };
	auto result1 = topologicalSort(jobs1, deps1);
	cout << "Elements in order \n";
	for (int job : result1) {
		cout << job << "\n";
	}
}