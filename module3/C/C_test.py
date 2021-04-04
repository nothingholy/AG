class WordReplcement:
    def __init__(self):
        self.dictionary = dict()
        self.incorrect = []
        self.distances = dict()

    def add_dict(self, temp):
        if self.dictionary.get(len(temp), None):
            self.dictionary[len(temp)].append(str(temp).lower())
        else:
            self.dictionary[len(temp)] = [str(temp).lower()]

    def add_incorrect(self, temp):
        self.incorrect.append(temp)

    def distance(self, s1, s2, maxDistance):
        s1, s2 = (s1, s2) if len(s1) <= len(s2) else (s2, s1)

        l1, l2 = len(s1), len(s2)

        transpositionRow = None
        prevRow = None

        curRow = [x for x in range(0, l1 + 1)]
        for rowNum in range(1, l2 + 1):
            transpositionRow, prevRow, curRow = prevRow, curRow, [rowNum] + [0] * l1

            if transpositionRow:
                if not any(cellValue < maxDistance for cellValue in transpositionRow):
                    return -1

            for colNum in range(1, l1 + 1):
                insertionCost = curRow[colNum - 1] + 1
                deletionCost = prevRow[colNum] + 1
                changeCost = prevRow[colNum - 1] + (0 if s1[colNum - 1] == s2[rowNum - 1] else 1)

                curRow[colNum] = min(insertionCost, deletionCost, changeCost)

                if 1 < rowNum <= colNum:
                    if s1[colNum - 1] == s2[colNum - 2] and s2[colNum - 1] == s1[colNum - 2]:
                        curRow[colNum] = min(curRow[colNum], transpositionRow[colNum - 2] + 1)

        return curRow[-1]

    def distance_words(self):
        for i in self.incorrect:
            self.distances[i] = []
            if self.dictionary.get(len(i), None):
                for j in self.dictionary[len(i)]:
                    strl = str(i).lower()
                    temp = self.distance(strl, str(j), 2)
                    self.distances[i].append((j, temp))

            if self.dictionary.get(len(i) + 1, None):
                for j in self.dictionary[len(i) + 1]:
                    strl = str(i).lower()
                    temp = self.distance(strl, str(j), 2)
                    self.distances[i].append((j, temp))

            if self.dictionary.get(len(i) - 1, None):
                for j in self.dictionary[len(i) - 1]:
                    strl = str(i).lower()
                    temp = self.distance(strl, str(j), 2)
                    self.distances[i].append((j, temp))

            self.distances[i].sort()
            
    def print(self):
        self.distance_words()
        
        res = ''
        for i in self.incorrect:
            temp = ''
            for j in self.distances[i]:
                if j[1] == 0:
                    if temp == '':
                        temp += i + ' - ok  '
                        break
                    temp = ''
                    temp += i + ' - ok  '
                    break
                elif j[1] == 1:
                    if temp == '':
                        temp += i + ' -> '
                    temp += j[0] + ', '

            if temp == '':
                temp += i + ' -?  '
            res += temp[:-2] + '\n'

        print(res)


flag = True
strl = input()
words = WordReplcement()
for i in range(int(strl)):
    temp = input()
    words.add_dict(temp)

while flag:
    try:
        another = input()
        if another == '':
            continue

        words.add_incorrect(another)

    except Exception:
        flag = False

words.print()