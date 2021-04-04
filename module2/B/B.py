class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def zag(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def zig(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    self.zig(x.parent)
                else:
                    self.zag(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.zig(x.parent.parent)
                self.zig(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.zag(x.parent.parent)
                self.zag(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.zag(x.parent)
                self.zig(x.parent)
            else:
                self.zig(x.parent)
                self.zag(x.parent)

    def search_helper(self, elem, key):
        if elem == None or key == elem.key:
            return elem

        if key < elem.key:
            return self.search_helper(elem.left, key)
        return self.search_helper(elem.right, key)

    def set_helper(self, elem, key):
        if key == elem.key:
            return elem
        elif key < elem.key:
            if elem.left == None:
                return elem
        elif key > elem.key:
            if elem.right == None:
                return elem

        if key < elem.key:
            return self.set_helper(elem.left, key)
        return self.set_helper(elem.right, key)

    def search(self, key):
        if not self.root:
            print('0')
            return
        prev = None
        vert = self.root
        while (vert != None):
            if vert.key < key:
                prev = vert
                vert = vert.right
            elif vert.key > key:
                prev = vert
                vert = vert.left
            elif vert.key == key:
                print('1 ' + vert.data)
                self.splay(vert)
                return
        print('0')
        self.splay(prev)

    def min(self):
        if not self.root:
            print('error')
            return
        temp = self.root
        while temp.left != None:
            temp = temp.left
        self.splay(temp)
        print(str(temp.key) + ' ' + temp.data)

    def max(self):
        if not self.root:
            print('error')
            return
        temp = self.root
        while temp.right != None:
            temp = temp.right
        self.splay(temp)
        print(str(temp.key) + ' ' + temp.data)

    def maximum(self, elem):
        while elem.right != None:
            elem = elem.right
        return elem

    def set(self, key, data_toset):
        if not self.root:
            print('error')
            return
        temp = self.set_helper(self.root, key)
        if temp.key == key:
            temp.data = data_toset
            self.splay(temp)
        else:
            self.splay(temp)
            print('error')

    def join(self, x, y):
        if x == None:
            return y
        if y == None:
            return x

        temp = self.maximum(x)
        self.splay(temp)
        temp.right = y
        y.parent = temp
        return temp

    def delete_elem(self, key):
        if not self.root:
            print('error')
            return
        elem = self.root
        temp = None
        x = None
        y = None
        # find necessary element
        temp2 = None
        while elem != None:
            if elem.key == key:
                temp = elem
            temp2 = elem
            if elem.key <= key:
                elem = elem.right
            else:
                elem = elem.left

        if temp == None:
            self.splay(temp2)
            print('error')
            return
        # splay for this element
        self.splay(temp)
        # make its children the current Merge tree
        if temp.right != None:
            x = temp.right
            x.parent = None
        else:
            x = None

        y = temp
        y.right = None
        temp = None
        if y.left != None:
            y.left.parent = None
        self.root = self.join(y.left, x)
        y = None

    def add(self, key, data):
        temp = self.search_helper(self.root, key)
        if temp:
            print('error')
            self.splay(temp)
            return
        elem = Node(key, data)
        y = None
        x = self.root

        while x != None:
            y = x
            if elem.key < x.key:
                x = x.left
            else:
                x = x.right

        elem.parent = y
        if y == None:
            self.root = elem
        elif elem.key < y.key:
            y.left = elem
        else:
            y.right = elem
        self.splay(elem)

    def print_nulls(self, temp):
        temp_str = '_ ' * (2 ** temp)

        return temp_str

    def print(self):
        if (self.root == None):
            print('_')
            return

        queue = []
        index = 0
        height = 0
        strpr = ''
        queue.append(self.root)

        while len(queue) != 0:
            end = 1

            for i in queue:
                if type(i) == type(self.root):
                    end = 0
            if end == 1:
                if index != 0:
                    strpr += '_ ' * (2 ** height - index)
                print(strpr[0:-1])
                return

            temp = queue.pop(0)

            if type(temp) == Node:
                if not temp.left:
                    queue.append(0)
                else:
                    queue.append(temp.left)

                if not temp.right:
                    queue.append(0)
                else:
                    queue.append(temp.right)

                index += 1
                if height == 0:
                    strpr += '[' + str(temp.key) + ' ' + str(temp.data) + ']\n'
                else:
                    if index == 2 ** height:
                        strpr += '[' + str(temp.key) + ' ' + str(temp.data) + ' ' + str(temp.parent.key) + ']\n'
                    else:
                        strpr += '[' + str(temp.key) + ' ' + str(temp.data) + ' ' + str(temp.parent.key) + '] '

            else:
                index += (2 ** temp)
                strpr += self.print_nulls(temp)
                queue.append(temp + 1)

                if index == 2 ** height:
                    strpr += '\n'

            if index == 2 ** height:
                height += 1
                index = 0

flag = True
tree = SplayTree()
while flag:
    try:
        strl = input()
        temp = strl.split(' ', 2)
        if strl == '':
            continue
        elif len(temp) == 3:
            if temp[0] == 'add':
                tree.add(int(temp[1]), temp[2])
            elif temp[0] == 'set':
                tree.set(int(temp[1]), temp[2])
            else:
                print('error')
        elif len(temp) == 2:
            if temp[0] == 'search':
                tree.search(int(temp[1]))
            elif temp[0] == 'delete':
                tree.delete_elem(int(temp[1]))
            else:
                print('error')
        elif len(temp) == 1:
            if temp[0] == 'print':
                tree.print()
            elif temp[0] == 'min':
                tree.min()
            elif temp[0] == 'max':
                tree.max()
            else:
                print('error')
        else:
            print('error')

    except Exception:
        flag = False
