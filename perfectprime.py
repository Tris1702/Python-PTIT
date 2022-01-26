"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i ==  0: return False
    return x > 1

def sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

def chr(x):
    for i in x:
        if i not in ['2','3','5','7']: return False
    return True

T = int(input())
for t in range(T):
    inp = input()
    n = int(inp)
    if (isPrime(n) and isPrime(int(inp[::-1])) and isPrime(sum(inp)) and chr(inp)):
        print('Yes')
    else: print('No')