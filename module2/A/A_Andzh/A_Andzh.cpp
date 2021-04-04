#include <iostream>
#include <vector>
#include <cmath>
#include <string>


const unsigned int Mersen = 2147483647;
const unsigned short nums[50] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229 };


class BitArray {
	std::vector<bool> _bits;

public:
	BitArray() = default;

	BitArray(unsigned int &m) {
		_bits.resize(m);
	}

	unsigned int size() {
		return _bits.size();
	}

	void set(unsigned int &index) {
		_bits[index] = 1;
	}

	bool get(unsigned int &index) {
		return _bits[index];
	}

	void print() {
		std::string out = "";
		for (const auto &i : _bits) {
			if (i) {
				out += '1';
			}
			else {
				out += '0';
			}
		}
		std::cout << out << std::endl;
	}

	~BitArray() {
		_bits.clear();
	}
};


class BloomFilter {
	unsigned int _k;
	bool _isSet = false;
	BitArray _bits;

	unsigned int hash(uint64_t &key, unsigned int i) {
		unsigned int res = ((((i + 1) * (key % Mersen)) % Mersen + nums[i]) % Mersen) % _bits.size();
		return res;
	}

public:
	BloomFilter() = default;

	BloomFilter(unsigned int &m, unsigned int &k) {
		_bits = BitArray(m);

		this->_k = k;
		this->_isSet = true;
	}

	bool isSet() { return this->_isSet; }

	void add(uint64_t &key) {
		for (unsigned int i = 0; i < _k; ++i) {
			unsigned int index = hash(key, i);
			_bits.set(index);
		}
	}

	bool search(uint64_t &key) {
		for (unsigned int i = 0; i < _k; ++i) {
			unsigned int index = hash(key, i);
			if (!_bits.get(index)) {
				return false;
			}
		}
		return true;
	}

	void print() {
		_bits.print();
	}

	~BloomFilter() = default;
};


int main() {
	int n;
	double p;
	unsigned int m, k;

	BloomFilter bf;

	std::string str = "";
	while (std::cin >> str) {
		try {
			if (str == "") {
				continue;
			}

			if (!bf.isSet() && str == "set") {
				std::cin >> n >> p;

				if (n <= 0 || p <= 0 || p > 1) {
					throw(std::exception());
				}

				m = round(-n * log2(p) / log(2));
				k = round(-log2(p));

				if (m <= 0 || k <= 0) {
					throw(std::exception());
				}

				std::cout << m << ' ' << k << std::endl;
				bf = BloomFilter(m, k);
			}
			else if (bf.isSet() && str != "set") {
				if (str == "add") {
					uint64_t temp = 0;
					std::cin >> temp;

					bf.add(temp);
				}
				else if (str == "search") {
					uint64_t temp = 0;
					std::cin >> temp;

					std::cout << bf.search(temp) << std::endl;
				}
				else if (str == "print") {
					bf.print();
				}
				else {
					std::cin.ignore(128, '\n');
					throw(std::exception());
				}
			}
			else {
				std::cin.ignore(128, '\n');
				throw(std::exception());
			}
		}
		catch (std::exception e) {
			std::cout << "error" << std::endl;
			continue;
		}
	}

	return 0;
}