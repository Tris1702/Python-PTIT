"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
a = list(float(i) for i in input().split())
a.sort()
i = 1
j = len(a)-2
while a[i-1] == a[i]: i += 1
while a[j+1] == a[j]: j -= 1

sum = 0
for k in range(i, j+1): sum += a[k]
print('{:.2f}'.format(sum/(j-i+1)))

