def findMin(a, n):
    if n == 1:
        return a[0]
    elif n == 2:
        if a[0] < a[1]:
            return a[0]
        return a[1]
    else:
        abc = findMin(a[:n//2], n//2) 
        xyz = findMin(a[n//2:], n - n//2) 
        if xyz < abc:
            return xyz
        else:
            return abc

a = [-1,5,1,6,2,8,6,4,3,0]
n = len(a)
print(findMin(a, n))