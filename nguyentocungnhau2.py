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

num, cs = map(int,input().split())
dem = 0
for i in range(10**(cs-1), 10**cs):
    if gcd(i, num) == 1:
        if (dem == 10):
            dem = 0
            print()
        print(i, end = ' ')
        dem += 1
