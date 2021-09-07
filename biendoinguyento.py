"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math

prime = []

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return x > 1

def genPrime():
    for i in range(10**5):
        if isPrime(i):
            prime.append(i)
def BS(l, r, x):
    res = r
    while l <= r:
        mid = (l+r)//2
        if prime[mid] == x: return mid
        if prime[mid] < x:
            l = mid+1
        else:
            res = mid
            r = mid - 1
    return res


genPrime()
n = int(input())
a = list(int(i) for i in input().split())
a = set(a)
inc = [0]
dec = [0]
tmp = []

for i in a:
    if isPrime(i): 
        continue
    else:
        it1 = BS(0, len(prime)-1, i)
        it2 = it1 - 1
        # print (i, end = ' ')
        if it2 < 0:
            # print(prime[it1], end=' ')
            inc.append(prime[it1]-i)
        else:
            if abs(prime[it1] - i) < abs(prime[it2] - i):
                # print(prime[it1], end=' ')
                inc.append(prime[it1] - i)
            elif abs(prime[it1] - i) > abs(prime[it2] - i):
                # print(prime[it2], end=' ')
                dec.append(prime[it2]-i)
            else:
                tmp.append(i)
maxx = max(max(inc), max(dec))
for i in tmp:
    it1 = BS(0, len(prime)-1, i)
    if prime[it1]-i > maxx: inc.append(prime[it1]-i)
inc = set(inc)
dec = set(dec)
num1 = max(dec)
num2 = max(inc)
print(num1+num2)

