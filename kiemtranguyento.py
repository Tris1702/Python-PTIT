"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1

N, M = map(int, input().split())
res = []
for i in range(N):
    tmp = []
    for item in (input().split()):
        so = int(item)
        if (isPrime(so)):
            tmp.append(1)
        else:
            tmp.append(0)
    res.append(tmp)

for i in range(0, N):
    for j in range(0, M):
        print(res[i][j], end = ' ')
    print()