"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math

def isprime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: return False
    return x > 1

n,m = map(int, input().split())

maxx = 0
x = []
for i in range(n):
    l = list(int(x) for x in input().split())
    for j in l:
        if isprime(j):
            maxx = max(maxx, j)
    x.append(l)
res = []
for i in range(n):
    for j in range(m):
        if x[i][j] == maxx:
            res.append([i,j])
            
if len(res) == 0: print('NOT FOUND')
else:
    print(maxx)
    for tmp in res:
        print('Vi tri ['+str(tmp[0])+']['+str(tmp[1])+']')    
