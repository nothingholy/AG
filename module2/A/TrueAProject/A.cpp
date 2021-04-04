#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

const unsigned int Mersen = 2147483647;

class Array {
    std::vector<bool> bitarray;

public:
    Array() = default;

    Array(unsigned int &m) {
        this->bitarray.resize(m);
    }

    unsigned int size() {
        return this->bitarray.size();
    }

    void set(unsigned int &index) {
        this->bitarray[index] = 1;
    }

    bool get(unsigned int& index) {
        return this->bitarray[index];
    }

    void print() {
        std::string str = "";
        for (const auto &i : this->bitarray) {
            str += i ? "1" : "0";
        }
        std::cout << str << std::endl;
    }

    ~Array() = default;
};


class BloomFilter {
    unsigned int k;
    Array bitarray;
    std::vector<unsigned short> nums = {};

public:
    BloomFilter() = default;

    BloomFilter(unsigned int &m, unsigned int &k) {
        this->bitarray = Array(m);
        this->k = k;

        simple(k);
    }

    void simple(int i) {
        if (i < 5) {
            nums = { 2, 3, 5, 7, 11 };
        }
        else {
            unsigned int n = ceil(i * (log(i) + log(log(i))));

            for (unsigned int i = 0; i < n + 1; ++i) {
                nums.emplace_back(i);
            }

            nums[1] = 0;

            unsigned int iter = 2;
            while (iter <= n) {
                if (nums[iter] != 0) {
                    unsigned int multed = iter + iter;
                    while (multed <= n) {
                        nums[multed] = 0;
                        multed += iter;
                    }
                }
                iter++;
            }

            std::sort(nums.begin(), nums.end());
            nums.resize(std::unique(nums.begin(), nums.end()) - nums.begin());
            nums.erase(nums.begin());
        }
    }

    unsigned int hash(uint64_t &key, unsigned int i) {
        return ((((i + 1) * (key % Mersen)) % Mersen + nums[i]) % Mersen) % this->bitarray.size();
    }

    void add(uint64_t &key) {
        for (unsigned int i = 0; i < k; ++i) {
            unsigned int index = this->hash(key, i);
            this->bitarray.set(index);
        }
    }

    bool search(uint64_t &key) {
        for (unsigned int i = 0; i < k; ++i) {
            unsigned int index = this->hash(key, i);
            if (!this->bitarray.get(index)) {
                return false;
            }
        }
        return true;
    }

    void print() {
        this->bitarray.print();
    }

    ~BloomFilter() = default;
};

int main() {
    int n;
    double p;
    unsigned int m, k;
    bool Set = false;

    BloomFilter exp;

    std::string str = "";
    while (std::cin >> str) {
        try {
            if (str == "") {
                continue;
            }

            if (!Set && str == "set") {
                std::cin >> n >> p;

                if (n <= 0 || p <= 0 || p > 1) {
                    throw(std::exception());
                }

                m = round(-n * log2(p) / log(2));
                k = round(-log2(p));

                if (m <= 0 || k <= 0) {
                    throw(std::exception());
                }
                
                Set = true;
                std::cout << m << ' ' << k << std::endl;
                exp = BloomFilter(m, k);
            }
            else if (Set && str != "set") {
                if (str == "add") {
                    uint64_t temp = 0;
                    std::cin >> temp;

                    exp.add(temp);
                }
                else if (str == "search") {
                    uint64_t temp = 0;
                    std::cin >> temp;

                    std::cout << exp.search(temp) << std::endl;
                }
                else if (str == "print") {
                    exp.print();
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