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

n = int(input())
x = []
a = list(int(i) for i in input().split())
for i in a:
    if isPrime(i): x.append(i)
x.sort()
it = 0
for i in a:
    if isPrime(i):
        print(x[it], end = ' ')
        it += 1
    else: print(i, end = ' ')