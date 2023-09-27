class Node:
    def __init__(self, data, parent = None, left = None, right = None) -> None:
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class Tree():
    def __init__(self) -> None:
        self.head = None
        self._size = 0
        self._height = 0
        self._size = 0

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
            self._height = 1
        else:
            currentNode = self.head
            while True:

                if currentNode.data > value:
                    if currentNode.left == None:
                        if currentNode.right == None:
                            self._height += 1
                        self._size += 1
                        currentNode.left = Node(value)
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        if currentNode.left == None:
                            self._height += 1
                        self._size += 1
                        currentNode.right = Node(value)
                        break
                    else:
                        currentNode = currentNode.right

    def __len__(self):
        return self._size
           
    def __str__(self) -> str:
        def func(data, result: list):
            result.append(data.data)
            # print(result)
            if data.left == data.right == None:
                return result
            else:
                if data.left != None:
                    func(data.left, result)
                if data.right != None:
                    func(data.right, result)
            
            return result
        return str(func(self.head, []))
    
    def height(self):
        return self._height
    
tree = Tree()
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.insert(7)
tree.insert(8)
print(tree.height())
print(len(tree))
print(tree)