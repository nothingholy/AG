class SearchElem:
    def __init__(self):
        self.elems = dict()
        self.arrays = []
        self.index = 0

    def initArrays(self, k, n):
        for i in range(k):
            self.arrays.append([0] * n)

    def add(self, temp):
        for i in range(len(temp)):
            self.arrays[self.index][i] = int(temp[i])
        self.index += 1

    def algorythm(self):
        if self.index == 1:
            print(self.arrays[0][0])
            return

        for i in self.arrays[0]:
            self.elems[i] = 1

        for i in range(1, len(self.arrays)):
            unique = dict()
            for j in range(len(self.arrays[i])):

                index = self.arrays[i][j]

                temp = self.elems.get(index, None)
                if temp:
                    if not unique.get(index, None):
                        self.elems[index] += 1 
                    unique[index] = 1

                    if self.elems[index] == self.index:
                        print(index)
                        return

        print('not found')


n = 0 
k = 0
alg = SearchElem()


strl = input()
temp = strl.split()

k = int(temp[0])
n = int(temp[1])
if k and n:
    alg.initArrays(k, n)

    for i in range(k):
        strl = input()
        temp = strl.split()

        alg.add(temp)

    alg.algorythm()
else:
    print('not found')

# Complexity: O(k * n), так как нужно пройти k массивов размерности n
# Memory: O(n), так как создаем словарь максимального размера n
# Используются словари (время обращения по ключу - O(1))
# На проверке очередного массива создается словарь для проверки повторного присутствия элемента в массиве
# В него добавляются только те элементы, которые могут быть ответами
# + итерация начинается с проверки второго массива
# тип можно проверять, если на данном массиве мы не встречали элемент из словаря, то его можно удалить из словаря
# облегчит память
# но заберет время