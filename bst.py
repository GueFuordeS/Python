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
    

    def remove(self, element):
        if self.data == element:
            if self.left != None and self.left.data != None:
                self.data = self.left.data
                tree = None
                if self.left.right != None:
                    tree = self.left.right
                self.left = self.left.left
                if tree:
                    self._addall(tree)
            elif self.right != None:
                self.data = self.right.data
                tree = None
                if self.right.left != None:
                    tree = self.right.left
                self.right = self.right.right
                if tree:
                    self._addall(tree)
            else:
                self.data = None
        else:
            if self.left != None:
                self.left.remove(element)
            if self.right != None:
                self.right.remove(element)
    
    
    def _addall(self, tree):
        if tree.data != None:
            self.insert(tree.data)
            if tree.left != None:
                self._addall(tree.left)
            if tree.right != None:
                self._addall(tree.right)

    
    def preorder(self):
        retorno = []
        if self.data != None:
            retorno.append(self.data)
            if self.left != None:
                retorno += self.left.preorder()
            if self.right != None:
                retorno += self.right.preorder()
        return retorno


    def inorder(self):
        retorno = []
        if self.data != None:
            if self.left != None:
                retorno += self.left.inorder()
            retorno.append(self.data)
            if self.right != None:
                retorno += self.right.inorder()
        return retorno


    def posorder(self):
        retorno = []
        if self.data != None:
            if self.left != None:
                retorno += self.left.posorder()
            if self.right != None:
                retorno += self.right.posorder()
            retorno.append(self.data)
        return retorno


    def height(self):
        retorno = 0
        if self.data != None:
            retorno += 1
            if self.left != None and self.right != None:
                retorno += max(self.left.height(), self.right.height())
            elif self.left != None:
                retorno += self.left.height()
            elif self.right != None:
                retorno += self.right.height()
        return retorno


    def maximum(self):
        max = self.data
        if self.right != None:
            if self.right.data != None:
                max = self.right.maximum()
        return max


    def minimum(self):
        min = self.data
        if self.left != None:
            if self.left.data != None:
                min = self.left.minimum()
        return min


    def __str__(self):
        retorno = ''
        if self.data != None:
            if self.left != None:
                retorno += self.left.__str__()
            retorno += ' ' + self.data.__str__() + ' '
            if self.right != None:
                retorno += self.right.__str__()
        return retorno


tree = Tree()

tree.insert(5)

tree.insert(1)

tree.insert(4)

tree2 = Tree(7)
tree2.insert(9)
tree2.insert(8)

tree._addall(tree2)


#print('Pre order Tree:', tree.preorder())
print('In order Tree:', tree.inorder())
#print('Pos order Tree:', tree.posorder())
tree.remove(5)
tree.remove(1)
tree.remove(8)
tree.remove(7)
tree.remove(4)
#print('Tree height:', tree.height())
print('Maximum element:', tree.maximum())
print('Minimum element:', tree.minimum())
print('In order Tree:', tree.inorder())
