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



T = int(input())
for t in range(T):
    n = int(input())
    dd = {}
    for i in range(10, n):
        x1 = str(i)[::-1]
        x2 = str(i)
        if x1 != x2:
            j = int(x1)
            if j >= n: continue
            if i not in dd:
                dd[j] = 1
                if isPrime(i) and isPrime(j):
                    print(i, j, end = ' ')
    print()
