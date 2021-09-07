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
            return 'NO'
    if x > 1: return 'YES'
    else: return 'NO'
T = int(input())
for t in range(T):
    s = input()
    num = 0
    for i in s:
        num += int(i)
    print(isPrime(num))