#pragma once

#include <algorithm>
#include <iterator>
#include <vector>

#include "transactions.hpp"
#include <numeric>

#define BEGIN_ACCOUNT "BACCT"

class Account {
	std::string name;
	std::vector<Transaction> transactions;

public:
	Account() : name({}), transactions({}){}
	Account(const std::string& name) : name(name), transactions({}){}

	const std::string& getName() {
		return name;
	}
	std::vector<Transaction>& getTransactions() {
		return transactions;
	}
	void addTransaction(Transaction& t) {
		transactions.push_back(t);
	}

	long double balance() {
		long double sum = std::accumulate(std::begin(transactions), std::end(transactions), 0, [](const long double& a, const Transaction& b) {
			return a + b.getAmount();
			});
		return sum;
	}

	friend std::ostream& operator<<(std::ostream& os, const Account& account) {
		os << BEGIN_ACCOUNT << " " << account.name << "\n";
	}
	friend std::istream& operator>>(std::istream& is, Account& account) {
		is >> account.name;
		return is;
	}
};