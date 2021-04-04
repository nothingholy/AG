import sys

class MyQueue(object):
    def __init__(self):
        self.cells = None
        self.size = 0
        self.index = 0
        self.indexPush = 0
        self.indexPop = 0
        self.flagTryResize = 0
        self.flagSize = False

    def setSize(self, size):
        if (self.flagTryResize != 0):
            Write.write('error' + '\n')
        else:
            self.cells = [None] * size
            self.size = size
            self.index = 0
            self.flagSize = True
            self.flagTryResize += 1

    def isEmpty(self):
        return self.index == 0

    def isNotFull(self):
        if (self.index < self.size):
            return True

    def push(self, item):
        if not self.flagSize:
            Write.write('error' + '\n')
        elif (self.isNotFull()):
            if(self.indexPush >= self.size):
                self.indexPush = 0
            self.cells[self.indexPush] = item
            self.indexPush += 1
            self.index += 1
        else:
            Write.write('overflow' + '\n')

    def pop(self):
        if not self.flagSize:
            Write.write('error' + '\n')
        elif (self.isEmpty()):
            Write.write('underflow' + '\n')
        else:
            if(self.indexPop >= self.size):
                self.indexPop = 0
            Write.write(self.cells[self.indexPop] + '\n')
            self.cells[self.indexPop] = None
            self.indexPop += 1
            self.index -= 1

    def print(self):
        if not self.flagSize:
            Write.write('error' + '\n')
        elif (self.isEmpty()):
            Write.write('empty' + '\n')
        else:
            indexPrint = self.indexPop
            i = 0
            while i < self.index:
                if indexPrint == self.size:
                    indexPrint = 0
                if not (self.cells[indexPrint] is None):
                    if i == self.index - 1:
                        Write.write(self.cells[indexPrint] + '\n')
                    else:
                        Write.write(self.cells[indexPrint] + ' ')
                    i += 1
                indexPrint += 1



try:
    Read = open(sys.argv[1])
    Write = open(sys.argv[2], 'w')
except Exception:
    print('error')
else:
    queue = MyQueue()
    for strl in Read:
        strl = strl[0:-1]
        temp = strl.split(' ', 2)
        print(temp)
        if (strl == ''):
            continue
        if (len(temp) > 2):
            Write.write('error' + '\n')
        elif (len(temp) == 1):
            if (temp[0] == 'pop'):
                queue.pop()
            elif (temp[0] == 'print'):
                queue.print()
            else:
                Write.write('error' + '\n')
        elif (len(temp) == 2):
            if (temp[0] == 'set_size'):
                if (temp[1].isdigit()):
                    queue.setSize(int(temp[1]))
                else:
                    Write.write('error' + '\n')
            elif (temp[0] == 'push'):
                queue.push(temp[1])
            else:
                Write.write('error' + '\n')

        else:
            Write.write('error' + '\n')