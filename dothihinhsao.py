"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
d ={}
for i in range(n-1):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = 1
    else: d[a] += 1
    if b not in d:
        d[b] = 1
    else: d[b] += 1

dem1 = 0
dem2 = 0
for i in d.keys():
    if d[i] == 1: dem1 += 1
    if d[i] == n-1: dem2 += 1
print('Yes' if (dem1 == n-1 and dem2 == 1) else 'No')