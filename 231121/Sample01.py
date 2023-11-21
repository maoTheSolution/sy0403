class Node:

    def __init__(self, num) -> None:
        self.data = num
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data : 
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, given) -> bool:
        con = False
        if self.left:
            self.left.search(given)
        if given == self.data:
            con = True
        if self.right:
            self.right.search(given)

        return con

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def printTree2(self):
        if self.right:
            self.right.printTree2()
        print(self.data)
        if self.left:
            self.left.printTree2()
        # print(self.data)

root = Node(7)
root.insert(3)
root.insert(9)
root.insert(1)
root.insert(4)
root.insert(8)
root.insert(10)


root.printTree()
print(root.search(4))