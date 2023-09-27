def addReciprocals(n):
    if n == 1:
        return 1
    else:
        return 1/n + addReciprocals(n-1)

print(addReciprocals(4))    