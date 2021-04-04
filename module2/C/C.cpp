#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>


class Heap {
	std::unordered_map<int64_t, std::pair<size_t, std::string>> items;
	std::vector<int64_t> indexes;

	size_t getParent(size_t i) { return (i - 1) / 2; }
	size_t getLeftChild(size_t i) { return 2 * i + 1; }
	size_t getRightChild(size_t i) { return 2 * i + 2; }
	
	bool hasParent(size_t i) { if (i == 0) return false; return getParent(i) >= 0; }
	bool hasLeftChild(size_t i) { return getLeftChild(i) < indexes.size(); }
	bool hasRightChild(size_t i) { return getRightChild(i) < indexes.size(); }
	
	int64_t parentKey(size_t i) { return indexes[getParent(i)]; }
	int64_t leftChildKey(size_t i) { return indexes[getLeftChild(i)]; }
	int64_t rightChildKey(size_t i) { return indexes[getRightChild(i)]; }

	void HeapifyUp(size_t i) {
		if (i == 0) return;
		while (hasParent(i) && parentKey(i) > indexes[i]) {
			std::swap(indexes[i], indexes[getParent(i)]);
			
			auto temp = items[indexes[i]];
			items[indexes[i]].first = items[parentKey(i)].first;
			items[parentKey(i)].first = temp.first;

			i = getParent(i);
		}
	}

	void HeapifyDown(size_t i) {
		while (hasLeftChild(i)) {
			size_t smallerChild = getLeftChild(i);
			if (hasRightChild(i) && rightChildKey(i) < leftChildKey(i)) smallerChild = getRightChild(i);

			if (indexes[i] < indexes[smallerChild]) break;

			std::swap(indexes[i], indexes[smallerChild]);

			auto temp = items[indexes[i]];
			items[indexes[i]].first = items[indexes[smallerChild]].first;
			items[indexes[smallerChild]].first = temp.first;

			i = smallerChild;
		}
	}
public:
	Heap() = default;

	~Heap() = default;

	void add(int64_t &key, std::string &data) {
		auto iter = items.find(key);
		if (iter != items.end()) throw(std::exception());

		items.emplace(key, std::make_pair(indexes.size(), data));
		indexes.push_back(key);
		HeapifyUp(indexes.size() - 1);
	}

	void set(int64_t key, std::string data) {
		if (items.find(key) == items.end()) throw(std::exception());
		items[key].second = data;
	}

	void remove(int64_t key) {
		if (items.find(key) == items.end()) throw(std::exception());

		size_t index = items[key].first;
		items.erase(key);
		indexes[index] = indexes[indexes.size() - 1];
		indexes.pop_back();

		if (indexes.size() > index) {
			items[indexes[index]].first = index;
			if (hasParent(index) && indexes[index] < parentKey(index)) HeapifyUp(index);
			else if (hasLeftChild(index)) HeapifyDown(index);
		}
	}
	
	void search(int64_t key) {
		if (items.find(key) == items.end()) {
			std::cout << 0 << std::endl;
			return;
		}

		std::cout << 1 << ' ' << items[key].first << ' ' << items[key].second << std::endl;
	}

	void min() {
		if (indexes.size() == 0) throw(std::exception());
		std::cout << indexes[0] << ' ' << 0 << ' ' << items[indexes[0]].second << std::endl;
	}

	void max() {
		if (indexes.size() == 0) throw(std::exception());

		size_t max = indexes.size() / 2;
		for (size_t i = max; i < indexes.size(); ++i) if (indexes[i] > indexes[max]) max = i;

		std::cout << indexes[max] << ' ' << max << ' ' << items[indexes[max]].second << std::endl;
	}

	void extract() {
		if (indexes.size() == 0) throw(std::exception());

		std::cout << indexes[0] << ' ' << items[indexes[0]].second << std::endl;
		
		items.erase(indexes[0]);
		indexes[0] = indexes[indexes.size() - 1];
		indexes.pop_back();
		if (indexes.size() > 1) {
			items[indexes[0]].first = 0;
			HeapifyDown(0);
		}
	}

	void print() {
		if (indexes.size() == 0) {
			std::cout << "_\n";
			return;
		}

		size_t height = 0;
		size_t index = 0;
		std::string res = "";
		for (size_t i = 0; i < indexes.size(); ++i) {
			index += 1;

			res +=  '[' + std::to_string(indexes[i]) + ' ' + items[indexes[i]].second;
			if (i == 0) { 
				res += "]\n";
				index = 0;
				height += 1;
				continue;
			}
			res += ' ' + std::to_string(parentKey(i)) + ']';

			if (index == 1 << height) {
				res += '\n';
				index = 0;
				height += 1;
			}
			else {
				res += ' ';
			}
		}

		if (index != 0) {
			for (int i = 0; i < (1 << height) - index; ++i) {
				res += "_ ";
			}
			res.erase(res.size() - 1);
			std::cout << res << std::endl;
			return;
		}
		
		std::cout << res;
	}
};


int main() {
	std::string line = "";
	Heap heap = Heap();
	while (std::cin >> line) {
		try {
			if (line == "") continue;

			if (line == "add") {
				int64_t key = 0;
				std::cin >> key;
				std::string data;
				std::cin >> data;
				heap.add(key, data);
				continue;
			}

			if (line == "set") {
				int64_t key = 0;
				std::cin >> key;
				std::string data;
				std::cin >> data;
				heap.set(key, data);
				continue;
			}

			if (line == "delete") {
				int64_t key = 0;
				std::cin >> key;
				heap.remove(key);
				continue;
			}

			if (line == "search") {
				int64_t key = 0;
				std::cin >> key;
				heap.search(key);
				continue;
			}

			if (line == "min") {
				heap.min();
				continue;
			}

			if (line == "max") { 
				heap.max();
				continue;
			}

			if (line == "extract") {
				heap.extract();
				continue;
			}

			if (line == "print") {
				heap.print();
				continue;
			}
		}
		catch (std::exception &e) {
			std::cout << "error\n";
		}
	}

	return 0;
}
