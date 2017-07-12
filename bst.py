class Tree:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == None:
            self.data = data
        elif data <= self.data:
            if self.left == None:
                self.left = Tree()
                self.left.parent = self
            self.left.insert(data)
        else:
            if self.right == None:
                self.right = Tree()
                self.right.parent = self
            self.right.insert(data)
    
    def __str__(self):
        if self.data != None:
            if self.left != None:
                self.left.__str__()
            print(self.data, end=' ')
            if self.right != None:
                self.right.__str__()


tree = Tree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.__str__()
print()
