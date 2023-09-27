def s(n, k):
    if n == k == 0:
        return 1
    elif ((n>0) and (k == 0)):
        return 0
    else: 
        return (s(n+1, k) - s(n, k-1))/(-n*s)


print(s(3,5))