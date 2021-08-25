"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

import math
def gcd(a, b):
    while (a > 0):
        if (a < b):
            a, b = b, a
        a = a % b
    return b

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

T = int(input())
for t in range(T):
    k = 1
    N = int(input())
    for i in range(2, N):
        if gcd(i, N) == 1:
            k = k + 1
    if isPrime(k):
        print('YES')
    else: print('NO')