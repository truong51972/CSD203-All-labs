def sumAll(n):
    if n == 1:
        return 1
    else:
        return n + sumAll(n-1)


print(sumAll(4))