def slices(s,n):
    if(len(s) < n or n == 0):
        raise ValueError("String is not long enough.")

    r = [list(map(int,s[i:i+n])) for i,x in enumerate(s) if len(s[i:i+n]) == n]

    return r


a = [1,2,3]
b = [2,3,4]
c = [x*y for x in a for y in b]
print(c)
