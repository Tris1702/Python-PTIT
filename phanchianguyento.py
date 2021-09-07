"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return x > 1

n = int(input())
a = list(int(i) for i in input().split())
dd = {}
b = []
for i in a:
    if i not in dd:
        dd[i] = 1
        if len(b) == 0: b.append(i)
        else: b.append(i+b[-1])
res = -1
for i in range(0,len(b)):
    if isPrime(b[i]) and isPrime(b[-1]-b[i]):
        res = i
        break
if res == -1: print("NOT FOUND")
else: print(res)