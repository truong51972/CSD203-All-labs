def isPalindrome(a, n):
    x = a[:n//2]
    if n % 2 == 0:
        y = a[n//2:]
    else:
        y = a[n//2+1:]
    y.reverse()
    return x == y
    

a = [1,2,3,5,3,5,3,2,1]
n = len(a)
print(isPalindrome(a,n))