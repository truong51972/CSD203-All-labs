def binarySearch(a, n, k):
    if k < a[n//2]: return binarySearch(a[:n//2], n//2, k)
    elif k > a[n//2]: return binarySearch(a[n//2:], n//2 +1, k) + n//2
    else: return n//2
    
a = [1,2,3,4,5,6,7,8,9]
n = len(a)
k = 9

print(binarySearch(a,n,int(input('k: '))))