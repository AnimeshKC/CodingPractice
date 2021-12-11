#pragma once

#include <string>
#include <ctime>
#include <iostream>
#define BEGIN_TRANSACTION "BTRANS"

std::string& trim(std::string& str) {
	str.erase(0, str.find_first_not_of(" \t\n"));
	str.erase(str.find_last_not_of(" \t\n") + 1);
	return str;
}
class Transaction {
	std::time_t transactionDate;
	std::string accountName;
	std::string memo;
	long double amount;

public:
	Transaction() : accountName({}), memo({}), amount{}, transactionDate(std::time(0)){}
	Transaction(const std::string &accountName, long double amount, const std::string &memo): accountName(accountName), amount(amount), memo(memo), transactionDate(std::time(0)){}

	const std::string& getAccountName() const {
		return accountName;
	}
	long getAmount() const {
		return amount;
	}
	const std::string& getMemo() const {
		return memo;
	}
	std::time_t getTransactionDate() const {
		return transactionDate;
	}

	friend std::ostream& operator<<(std::ostream& os, const Transaction& t);
	friend std::istream& operator>>(std::istream& is, Transaction& t);

};

std::ostream& operator<<(std::ostream& os, const Transaction& t) {
	os << BEGIN_TRANSACTION << " " << t.accountName << " " << t.transactionDate << " " << t.amount << " " << t.memo << "\n";
	return os;
}

std::istream& operator>>(std::istream& is, Transaction& t) {
	is >> t.accountName;
	is >> t.transactionDate;
	is >> t.amount;
	std::getline(is, t.memo);

	trim(t.memo);
	return is;
}
