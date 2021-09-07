"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

T = int(input())
for t in range(T):
    s = input()
    num = s[len(s)-4:]
    if isPrime(int(num)):
        print('YES')
    else: print('NO')