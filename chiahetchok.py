"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

count = 0
a, k, n = map(int, input().split())

st = (int(a/k) + 1) * k

for i in range(st, n+1, k):
    print(i-a, end = ' ')
    count = count + 1
if count == 0:
    print(-1)
else:
    print()

