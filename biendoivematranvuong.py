"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))

hbo = []
cbo = []
nn = n
mm = m
if n > m:
    for i in range(0, n, 2):
        hbo.append(i)
        n-= 1
        if n == m: break
if n < m:
    for i in range(1, m, 2):
        cbo.append(i)
        m-=1
        if n == m: break
for i in range(nn):
    if i in hbo: continue
    for j in range(mm):
        if j in cbo: continue
        print(a[i][j], end =' ')
    print()
