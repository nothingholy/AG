#include <iostream>
#include <vector>
#include <cmath>
#include <string>


const unsigned int Mersen = 2147483647;
const unsigned short nums[50] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229 };


class BitArray {
	std::vector<bool> bits;

public:
	BitArray() = default;

	BitArray(unsigned int &m) {
		bits.resize(m);
	}

	unsigned int size() {
		return bits.size();
	}

	void set(unsigned int &index) {
		bits[index] = 1;
	}

	bool get(unsigned int& index) {
		return bits[index];
	}

	void print() {
		std::string out = "";
		for (const auto &i : bits) {
			if (i) {
				out += '1';
			}
			else {
				out += '0';
			}
		}
		std::cout << out << std::endl;
	}

	~BitArray() = default;
};


class BloomFilter {
	unsigned int k;
	bool isSet = false;
	BitArray bits;

public:
	unsigned int hash(uint64_t &key, unsigned int i) {
		unsigned int res = ((((i + 1) * (key % Mersen)) % Mersen + nums[i]) % Mersen) % bits.size();
		return res;
	}

	BloomFilter() = default;

	BloomFilter(unsigned int &m, unsigned int &k) {
		bits = BitArray(m);

		this->k = k;
		this->isSet = true;
	}

	bool is_set() { return this->isSet; }

	void add(uint64_t &key) {
		for (unsigned int i = 0; i < k; ++i) {
			unsigned int index = hash(key, i);
			bits.set(index);
		}
	}

	bool search(uint64_t &key) {
		for (unsigned int i = 0; i < k; ++i) {
			unsigned int index = hash(key, i);
			if (!bits.get(index)) {
				return false;
			}
		}
		return true;
	}

	void print() {
		bits.print();
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

			if (!bf.is_set() && str == "set") {
				std::cin >> n >> p;

				if (n <= 0 || p <= 0 || p > 1) {
					std::cout << "error" << std::endl;
					continue;
				}

				m = round(-n * log2(p) / log(2));
				k = round(-log2(p));

				if (m <= 0 || k <= 0) {
					std::cout << "error" << std::endl;
					continue;
				}

				std::cout << m << ' ' << k << std::endl;
				bf = BloomFilter(m, k);
			}
			else if (bf.is_set() && str != "set") {
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
					std::cout << "error" << std::endl;
					continue;
				}
			}
			else {
				std::cin.ignore(128, '\n');
				std::cout << "error" << std::endl;
				continue;
			}
		}
		catch (std::exception e) {
			std::cout << "error" << std::endl;
			continue;
		}
	}

	return 0;
}
