#include <iostream>
#include <vector>

/*
hash: 990ba22653ea77451cb3da81c0f0c8bc
bytes: 153 11 162 38 83 234 119 69 28 179 218 129 192 240 200 188
type: linear probing
result: 234 119 28 69 83 162 240 179 11 38 218 129 192
*/

template <class T> class Node {
public:
    T key;
    Node * left = nullptr;
    Node * right = nullptr;

    Node(T key){
        this->key = key;
    }
};

void printEvenInOrder(Node<int>* root){
    if (!root){
        std::cout << "error" << std::endl;
        return;
    }
    std::vector<int> k;
    std::vector<Node<int>*> elems;
    elems.push_back(root);
    while(!elems.empty()){
        Node<int>* temp = elems.back();
        elems.pop_back();
        if (temp->key % 2 == 0) k.push_back(temp->key);

        if(temp->left) elems.push_back(temp->left);

        if (temp->right) elems.push_back(temp->right);
    }
    for (size_t i = 1; i < k.size(); ++i){
        for (size_t j = 0; j < k.size(); ++j) {
            if(k[j] > k[i]){
                auto temp = k[i];
                k[i] = k[j];
                k[j] = temp;
            }
        }
    }
    for(auto& i : k){
        std::cout << i << " ";
    }
};
/*
    Сomplexity: O(n) + O(n^2)
    Memory usage: O(n)
    Efficiency:

    RK format: 10/10
*/


