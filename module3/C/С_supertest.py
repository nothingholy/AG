def leven(s1, s2, maxDistance):
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

strl = 'jopa'
strl1 = 'johs'
print(leven(strl, strl1, 2))