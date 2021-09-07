"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
k = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if j < n-i-1: sum1 += a[i][j]
        if j > n-i-1: sum2 += a[i][j]
if abs(sum1-sum2) <= k: print('YES')
else: print('NO')
print(abs(sum1-sum2))
