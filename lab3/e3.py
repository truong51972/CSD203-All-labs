def findSum(a, n):
    if n == 1: return a[0]
    else:
        return a[n-1] + findSum(a,n-1)

a = [8,6,4,3,0]
n = len(a)
print(findSum(a, n))