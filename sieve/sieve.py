from math import sqrt

def sieve(num):
    arrsize = int(sqrt(num)) + 1
    arr = [True for x in range(arrsize)]
    for x in range(2,int(sqrt(num))):
        if arr[x] == True:
            for y in range(x*2,num,x):
                arr[y] = False
    return arr

#print(sieve(13))

