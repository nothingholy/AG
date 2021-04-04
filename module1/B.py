class MyStack(object):
    def __init__(self):
        self.cells = None
        self.size = 0
        self.index = 0
        self.flagTryResize = 0
        self.flagSize = False

    def setSize(self, size):
        if(self.flagTryResize != 0):
            print('error')
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
        if(self.flagSize == False):
            print('error')
        elif (self.isNotFull()):
            self.cells[self.index] = item
            self.index += 1
        else:
            print('overflow')

    def pop(self):
        if(self.flagSize == False):
            print('error')
        elif (self.isEmpty()):
            print('underflow')
        else:
            print(str(self.cells[self.index - 1]))
            self.cells[self.index - 1] = ''
            self.index -= 1

    def print(self):
        if (self.flagSize == False):
            print('error')
        elif (self.isEmpty()):
            print("empty")
        else:
            i = 0
            while i < self.index:
                if(i == self.index - 1):
                    print(str(self.cells[i]))
                else:
                    print(str(self.cells[i]),end=' ')
                i += 1


flag = True
stack = MyStack()
while flag:
    try:
        strl = input()
        temp = strl.split(' ', 2)
        if(strl == ''):
            continue
        if (len(temp) > 2):
            print('error')
        elif(len(temp) == 1):
            if (temp[0] == 'pop'):
                stack.pop()
            elif(temp[0]=='print'):
                stack.print()
            else:
                print("error")
        elif(len(temp) == 2):
            if (temp[0] == 'set_size'):
                if(temp[1].isdigit()):
                    stack.setSize(int(temp[1]))
                else:
                    print('error')
            elif (temp[0] == 'push'):
                stack.push(temp[1])
            else:
                print("error")

        else:
            print('error')

    except Exception:
        flag = False
