"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
primeDigits = ['2', '3', '5', '7']

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1

T = int(input())

for t in range(T):
    s = input()
    check = True
    for i in range(0, len(s)):
        if isPrime(i):
            if s[i] not in primeDigits:
                check = False
                break
        else:
            if s[i] in primeDigits:
                check = False
                break
    if check: print('YES')
    else: print('NO')