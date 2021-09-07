"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math

def gcd(a, b):
    while (a > 0):
        if a < b:
            a, b = b, a
        a %= b
    return b

T = int(input())
for t in range(T):
    s = input()
    num1 = int(s)
    num2 = int(s[::-1])
    if gcd(num1, num2) == 1:
        print('YES')
    else:
        print('NO')