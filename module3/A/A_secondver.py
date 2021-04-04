import math

class Backpack:
    def __init__(self):
        self.max_weight = None
        self.weights = list()
        self.costs = list()
        self.ans = list()
        self.coefficient = 1
        self.matrix = []

    def maxWeight(self, temp):
        self.max_weight = temp
        self.coefficient = temp

    def add(self, weight, cost):
        self.weights.append(weight)
        self.costs.append(cost)

    def matrixInit(self):
        for i in range(1, len(self.weights) - 1):
                    temp = math.gcd(self.weights[i], self.weights[i + 1])

                    if temp < self.coefficient:
                        self.coefficient = temp

        if self.max_weight != 0:
            if self.max_weight % self.coefficient == 0:
                self.max_weight = int(self.max_weight / self.coefficient)

                for i in range(len(self.weights)):
                    self.weights[i] = int(self.weights[i] / self.coefficient)

        for i in range(len(self.costs) + 1):
            self.matrix.append([0] * (self.max_weight + 1))


    def algorythm(self):
        self.matrixInit()
        for i in range(1, len(self.costs) + 1):
            for j in range(self.max_weight + 1):
                if self.weights[i - 1] <= j:
                    self.matrix[i][j] = max(self.matrix[i - 1][j], self.matrix[i - 1][j - self.weights[i - 1]] + self.costs[i - 1])
                else:
                    self.matrix[i][j] = self.matrix[i - 1][j]

        max_cost = 0
        max_weight = 0
        i = len(self.costs)
        j = self.max_weight
   
        while self.matrix[i][j]:
            if self.matrix[i][j] != self.matrix[i - 1][j]:
                    self.ans.append(i)
                    max_cost += self.costs[i - 1]
                    max_weight += self.weights[i - 1]
                    j -= self.weights[i - 1]

            i -= 1

        self.ans.sort()
        return [max_weight * self.coefficient, max_cost]

    def print(self):
        temp = self.algorythm()
        print(temp[0], temp[1])
        for i in self.ans:
            print(i)



flag = True
init = False
back = Backpack() 

while flag:
    try:
        str = input()
        temp = str.split(' ', 2)

        if (str == ''):
            continue

        if not init and len(temp) == 1:
            if temp[0].isdigit():
                if int(temp[0]) < 0:
                    print('error')
                else:
                    back.maxWeight(int(temp[0]))
                    init = True
            else:
                print('error')
        elif init and len(temp) == 2:
                if temp[0].isdigit() and temp[1].isdigit():
                    if int(temp[0]) < 0 or int(temp[1]) < 0:
                        print('error')
                    else:
                        back.add(int(temp[0]), int(temp[1]))
                else:
                    print('error')
        else:
            print('error')

    except Exception:
        flag = False 

if init:
    back.print()