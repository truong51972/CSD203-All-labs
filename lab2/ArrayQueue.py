class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self) -> None:
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def clear(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def isEmpty(self):
        return self._size == 0
    
    def first(self):
        if self.isEmpty():
            raise IndexError('Array is empty')
        return self._data[self._front]

    def dequeue(self):
        result = self.first()
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return result
    
    def enqueue(self, value):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = value
        self._size += 1

    def _resize(self, newCap):
        oldData = self._data
        self._data = [None]*newCap
        walk = self._front
        for k in range(self._size):
            self._data[k] = oldData[walk]
            walk = (walk + 1)%len(oldData)
        self.font = 0

    def traversal(self):
        walk = self._front
        result = ''
        for k in range(self._size):
            result += str(self._data[walk])
            if k < self._size -1:
                result += ', '
            walk = (walk + 1)%len(self._data)
        print('[{}]'.format(result))

    def __str__(self):
        walk = self._front
        result = ""
        for k in range(self._size):
            
            if str(type(self._data[walk])) == "<class 'int'>":
                result += str(self._data[walk])
            elif str(type(self._data[walk])) == "<class 'str'>":
                result += "'"
                result += str(self._data[walk])
                result += "'"
            else:
                result += "<{0} object at {1}>".format(str(type(self._data[walk]))[7:-1], hex(id(self._data[walk])))
            if k < self._size -1:
                result += ', '

            walk = (walk + 1)%len(self._data)
        return '[{}]'.format(result)

    def ctvBinary(self, afterDot):
        try:

            oldData = self._data
            walk = self._front
            result = 0
            for k in range(self._size):
                if walk >= 2:
                    kurukuru = oldData[walk]*(10**(-(walk -1)))
                    result += kurukuru
                    walk = (walk + 1)%len(oldData)
                else:
                    walk = (walk + 1)%len(oldData)

            result = round(result, self._size - 2)
            self.clear()

            self.enqueue(0)
            self.enqueue('.')
            for i in range(afterDot):
                result *= 2
                if (result == 1):
                    self.enqueue(1)
                    break
                elif (result > 1):
                    self.enqueue(1)
                    result -= 1
                else:
                    self.enqueue(0)
        except:
            print('Error!')
                
if __name__ == '__main__':
    s = ArrayQueue()
    s.enqueue(0)
    s.enqueue('.')
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.traversal()
    s.ctvBinary(20)
    print(s)