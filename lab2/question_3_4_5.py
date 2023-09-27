from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

s1 = ArrayQueue()

s1.enqueue(1)
s1.enqueue('2')
s1.enqueue(ArrayQueue())
s1.enqueue([])
print(s1)

s2 = ArrayStack()

s2.push(1)
s2.push('2')
s2.push(ArrayStack())
s2.push([])
s2.push()

print(s2)