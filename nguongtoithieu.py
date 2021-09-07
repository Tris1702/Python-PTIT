"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

s = input()
k = int(input())
a = {}
for i in range(1, len(s), 2):
    so = int(s[i-1])*10+int(s[i])
    if so not in a:
        a[so] = 1
    else:
        a[so] += 1
res = sorted(a.items(), key = lambda x: x[0])
check = 0
for i in res:
    if i[1] >= k:
        check = 1
        print(i[0], i[1])
if check == 0:
    print('NOT FOUND')