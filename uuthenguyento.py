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
    if isPrime(len(s)):
        count_nt = 0
        for i in s:
            if i in ('2', '3', '5', '7', '9'):
                count_nt += 1
        if count_nt > (len(s) - count_nt):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')