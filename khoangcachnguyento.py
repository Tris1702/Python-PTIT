"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1

noPrime = [2]
so = 2
while (len(noPrime) < 1000):
    so = so + 1
    if (isPrime(so)):
        noPrime.append(so)

N, X = map(int, input().split())
for i in range(0, N):
    print(X, end = ' ')
    X = X + noPrime[i]
print(X)