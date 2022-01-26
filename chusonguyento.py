"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0: return False
    return x > 1

def check(s):
    dem = 0
    if isPrime(len(s)) == False: return False
    for i in s:
        if isPrime(int(i)): dem+=1
    return dem*2 > len(s)

n = int(input())

for i in range(n):
    if check(input()):
        print('YES')
    else: print('NO')

