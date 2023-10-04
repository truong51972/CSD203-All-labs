class Node:
    def __init__(self, value, left = None, right = None, parent = None, IsParentLeft = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.IsParentLeft = IsParentLeft

class Tree():
    def __init__(self) -> None:
        self._head = None
        self._size = 0
        self._height = 0

    def isEmpty(self):
        return self._size == 0
    
    def clear(self):
        self._head = None
        self._size = 0
        self._height = 0

    def search(self, value):
        def __func(node, value0, x, y):
            currentNode = node
            if currentNode.value == value0:
                return currentNode, x, y
            else:
                if currentNode.left != None:
                    if (a:= __func(currentNode.left, value0, x, y+1)) != None:
                        return a

                if currentNode.right != None:
                    if(b := __func(currentNode.right, value0, x+1, y+1)) != None:
                        return b        

        if self._size == 0:
            return None
        else:
            return __func(self._head, value, 0, 0)

    def insert(self, value):
        if self._head == None:
            self._head = Node(value)
            self._size += 1
        else:
            currentNode = self._head
            while True:
                if currentNode.value > value:
                    if currentNode.left == None:
                        self._size += 1
                        currentNode.left = Node(value, parent=currentNode, IsParentLeft=True)
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        self._size += 1
                        currentNode.right = Node(value, parent=currentNode, IsParentLeft=False)
                        break
                    else:
                        currentNode = currentNode.right

    def __len__(self):
        return self._size

    def breadth(self):
        def __func(node:Node, result: dict, level:int):
            result[level] = result.get(level, [])
            result[level].append(node.value)
            if node.left == node.right == None:
                return result
            else:
                if node.left != None:
                    __func(node.left, result, level+1)
                if node.right != None:
                    __func(node.right, result, level+1)
            
            return result
        
        if self._size == 0:
            return '{}'
        else:
            returnDict = __func(self._head, {}, 0)
            result = []
            for i in range(len(returnDict)):
                result.extend(returnDict[i])
            return result
    
    def preOrder(self): 
        def __func(node, result: list):
            result.append(node.value)
            if node.left == node.right == None:
                return result
            else:
                if node.left != None:
                    __func(node.left, result)
                if node.right != None:
                    __func(node.right, result)
            
            return result
        
        if self._size == 0:
            return '[]'
        else:
            return __func(self._head, [])
        
    def postOrder(self): 
        def __func(node, result: list):
            if node.left == node.right == None:
                result.append(node.value)
                return result
            else:
                if node.left != None:
                    __func(node.left, result)
                if node.right != None:
                    __func(node.right, result)
                result.append(node.value)
            
            return result
        
        if self._size == 0:
            return '[]'
        else:
            return str(__func(self._head, []))

    def inOrder(self): 
        def __func(node, result: list):
            if node.left == node.right == None:
                result.append(node.value)
                return result
            else:
                if node.left != None:
                    __func(node.left, result)
                result.append(node.value)
                if node.right != None:
                    __func(node.right, result)
            return result
        
        if self._size == 0:
            return '[]'
        else:
            return str(__func(self._head, []))
        
    def __str__(self) -> str:
        def __func(node, result: list):
            result.append(node.value)
            # print(result)
            if node.left == node.right == None:
                return result
            else:
                if node.left != None:
                    __func(node.left, result)
                if node.right != None:
                    __func(node.right, result)
            
            return result
        if self._size == 0:
            return '[]'
        else:
            return __func(self._head, [])
    
    def count(self):
        return self._size
    
    def deleteValue(self, value):
        def __func(previousNode ,node, value0):
            if node == None:
                print('Empty Tree!')
                return
            
            if node.value == value0:
                if node.left == node.right == None:
                    print(node.value)
                    if node.IsParentLeft:
                        previousNode.left = None
                    else:
                        previousNode.right = None
                    self._size -= 1
                elif node.left != None and node.right == None:
                    if node.IsParentLeft:
                        previousNode.left = None
                    else:
                        previousNode.right = None
                    self._size -= 1
                elif node.right != None and node.left == None:
                    if node.IsParentLeft:
                        previousNode.left = None
                    else:
                        previousNode.right = None
                    self._size -= 1
                else:
                    def __func0(node, result: list):
                        if node.left == node.right == None:
                            result.append(node)
                            return result
                        else:
                            if node.left != None:
                                __func0(node.left, result)
                            result.append(node)
                            if node.right != None:
                                __func0(node.right, result)
                        return result

                    listInOrder = __func0(node, [])
                    for i, id in enumerate(listInOrder):
                        if id.value == value:
                            result = listInOrder[i+1]
                            break

                    if result.IsParentLeft:
                            result.parent.left = None
                    else:
                        result.parent.right = None

                    if value == self._head.value:
                        result.left = self._head.left
                        result.right = self._head.right
                        self._head = result
                    else:
                        if node.IsParentLeft:
                            node.parent.left = result
                        else:
                            node.parent.right = result

                        result.parent = node.parent
                        result.IsParentLeft = node.IsParentLeft

                        result.left = node.left
                        result.right = node.right
                    self._size -= 1
            else:
                if node.left == node.right == None:
                    return
                if node.left != None:
                    __func(node, node.left, value0)
                if node.right != None:
                    __func(node, node.right, value0)
                    

        __func(None, self._head, value)

    def min(self):
        if self._size == 0:
            return None
        else:
            current = self._head
            while current.left != None:
                current = current.left
            
            return current.value

    def max(self):
        if self._size == 0:
            return None
        else:
            current = self._head
            while current.right != None:
                current = current.right
            
            return current.value

    def sumTree(self):
        return sum(self.preOrder())
    
    def averageTree(self):
        return sum(self.preOrder())/self._size
    
    def height(self):
        return self.__heightOfNode(self._head)
    
    def biggestPath(self): 
        def __func(node: Node, result: int):
            result += node.value
            if node.left == node.right == None:
                return result
            else:
                if node.left != None and node.right != None:
                    left = __func(node.left, result)
                    right = __func(node.right, result)
                    if left > right: return left
                    return right
                elif node.left == None and node.right != None:
                    return __func(node.right, result)
                elif node.left != None and node.right == None:
                    return __func(node.left, result)
        
        if self._size == 0:
            return None
        else:
            return __func(self._head, 0)
        
    def __heightOfNode(self, node: Node):
        if node is None:
            return 0
        
        left = self.__heightOfNode(node.left)
        right = self.__heightOfNode(node.right)

        return max(left, right) + 1
    
    def isAVL(self):
        def func(node: Node):
            if node is None:
                return True

            left = self.__heightOfNode(node.left)
            right = self.__heightOfNode(node.right)
            
            if abs(left - right) < 2:
                a = func(node.left)
                b = func(node.right)
                print(a, b, a==b)
                return a == b
            else:
                return False
            
        return func(self._head)

        
# Let us create following BST
    #          50
    #       /     \
    #      30      70
    #     /  \    /  \
    #   20   40  60   80
    #    \   /
    #    25 35
tree = Tree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
# tree.insert(60)
# tree.insert(80)
tree.insert(35)
# tree.insert(25)

# print(tree.isEmpty())
# print(len(tree))
# print('Breadth: ' + tree.breadth())
# print(f'In-order: {tree.inOrder()}')
print(f'Pre-order: {tree.preOrder()}')
# print(f'Breadth: {tree.breadth()}')
# print('Post-order: ' + tree.postOrder())
# print(tree.search(20))
# print(tree.count())
# tree.deleteValue(51)
# print(f'Pre-order: {tree.preOrder()}')
# print('Height of tree: ' + str(tree.height()))
# print(tree.min())
# print(tree.max())
# print(tree.sumTree())
# print(tree.averageTree())
print(tree.biggestPath())
print(tree.isAVL())