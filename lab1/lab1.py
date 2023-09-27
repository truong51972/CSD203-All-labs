class SinglyLinkedList:
    class Node:
        def __init__(self, data= None, next= None) -> None:
            self.data = data
            self.next = next

    def __init__(self) -> None:
        self._head = None

    def size(self):
        if self._head == None: return 0
        else:
            size = 0
            currNode = self._head
            while True:
                size += 1
                if currNode.next == None: break
                currNode = currNode.next
            return size

    def reverse(self):
        copyOfList = self._head
        self._head = None

        while True:
            self.addToHead(copyOfList.data)
            if copyOfList.next == None: break
            copyOfList = copyOfList.next

    def getHeadID(self):
        return self._head
    
    def addToHead(self, x):
        if self._head == None:
            self._head = self.Node(data= x)
        else:
            newNode = self.Node(data= x, next= self._head)
            self._head = newNode
    
    def addToTail(self, x):
        if self._head == None:
            self._head = self.Node(data= x)
        else:
            currNode = self._head
            newNode = self.Node(data= x)
            while True:
                if currNode.next == None:
                    currNode.next = newNode
                    break
                currNode = currNode.next


    def addAfter(self, p, x):
        currNode = self._head
        for i in range(p):
            if currNode.next == None: break
            currNode = currNode.next

        newNode = self.Node(data=x, next=currNode.next)
        currNode.next = newNode

    def traverse(self):
        currNode = self._head
        print('list: [', end='')
        while True:
            print(currNode.data, end=', ')
            if currNode.next == None: break
            currNode = currNode.next
        print(']')

    def deleteFromHead(self):
        if self._head == None: return None
        else:
            firstValue = self._head.data
            self._head = self._head.next
            return firstValue

    def deleteFromTail(self):
        currNode = self._head
        while True:
            if currNode.next.next == None:
                lastValue = currNode.next.data
                currNode.next = None
                break
            currNode = currNode.next
        return lastValue

    def deleteAfter(self, p):
        if p >= (self.size() - 1):
            print('Out of Range! must in [1, n-1]')
        else:
            currNode = self._head
            for i in range(p):
                currNode = currNode.next

            valueAfterNodeP = currNode.next.data
            currNode.next = currNode.next.next
            return valueAfterNodeP
        
    def deleteByValue(self, x):
        if self._head.data == x:
            self._head = self._head.next
        else:
            currNode = self._head

            while True:
                if currNode.next == None: break
                if currNode.next.data == x:
                    currNode.next = currNode.next.next
                    break

                currNode = currNode.next

    def seach(self, x):
        currNode = self._head
        index = 0
        while True:
            if currNode.data == x:
                print(f"data: {x}, index: {index}")
                return
            
            if currNode.next == None: break
            currNode = currNode.next
            index += 1
        print(f"{x} not found!")

    def count(self):
        return self.size()

    def deleteByIndex(self, p):
        if p in range(self.size()):
            if p == 0:
                self.deleteFromHead()
            else:
                currNode = self._head
                for i in range(p-1):
                    currNode = currNode.next

                currNode.next = currNode.next.next
        else: print('Out of range!')

    def sort(self):
        currNode = self._head
        isSwap = False
        while True:
            if currNode.next.data < currNode.data:
                isSwap = True
                tempNode = currNode.next
                currNode.next = currNode.next.next
                
                self.insertIntoSortedList(tempNode.data)
            if not isSwap:
                isSwap = False
                currNode = currNode.next
            if currNode.next == None: break
                

    def deleteByNode(self, node):
        
        pass
    def toArray(self):
        currNode = self._head
        arrayOfLinkedList = []
        while True:
            arrayOfLinkedList.append(currNode.data)

            if currNode.next == None: break
            currNode = currNode.next
        return arrayOfLinkedList
    
    def mergeOrderedList(self, linkedList):
        copyOfCurrentList = self._head
        self._head = None

        while True:
            if linkedList != None and copyOfCurrentList != None:
                if linkedList.data < copyOfCurrentList.data:
                    self.addToHead(linkedList.data)
                    linkedList = linkedList.next
                else: 
                    self.addToHead(copyOfCurrentList.data)
                    copyOfCurrentList = copyOfCurrentList.next
            elif linkedList != None:
                self.addToHead(linkedList.data)
                linkedList = linkedList.next
            elif copyOfCurrentList != None:
                self.addToHead(copyOfCurrentList.data)
                copyOfCurrentList = copyOfCurrentList.next
            else: break
        self.reverse()
    def addBefore(self, p, x):
        if p == 0:
            self.addToHead(x)
        else:
            self.addAfter(p-1, x)

    def linkNewLinkedListAtTheEnd(self, linkedList):
        currNode = self._head
        while True:
            if currNode.next == None: break
            currNode = currNode.next

        while True:
            data = linkedList.deleteFromHead()
            if (data != None):
                currNode.next = self.Node(data= data)
                currNode = currNode.next

            else: break

    def max(self):
        currNode = self._head
        maxValue = currNode.data

        while True:
            if currNode.data > maxValue:
                maxValue = currNode.data

            if currNode.next == None: break
            currNode = currNode.next
        
        return maxValue
    
    def min(self):
        currNode = self._head
        minValue = currNode.data

        while True:
            if currNode.data < minValue:
                minValue = currNode.data

            if currNode.next == None: break
            currNode = currNode.next
        
        return minValue
    
    def sum(self):
        currNode = self._head
        total = 0
        while True:
            total += currNode.data
            if currNode.next == None: break
            currNode = currNode.next
        return total
    
    def avg(self):
        return self.sum()/self.size()

    def sorted(self):
        currNode = self._head

        while True:
            if currNode.next == None: break

            if currNode.next.data < currNode.data: return False
            currNode = currNode.next

        return True
    
    def insertIntoSortedList(self, x):
        newNode = self.Node(data=x)
        if newNode.data <= self._head.data:
            newNode.next = self._head
            self._head = newNode
        else:
            currNode = self._head
            while True:
                if currNode.next == None: break
                if currNode.next.data >= newNode.data: break
                currNode = currNode.next

            newNode.next = currNode.next
            currNode.next = newNode

    def isTheSame(self, linkedList):
        currNode = self._head

        while True:
            if not(currNode.data == linkedList.deleteFromHead()): return False
            if currNode.next == None: return True
            currNode = currNode.next

if __name__ == '__main__':
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()

    for i in range(10):
        list1.addToHead(i)
        list2.addToHead(i)
    list1.deleteFromHead()
    print(list1.isTheSame(list2))
