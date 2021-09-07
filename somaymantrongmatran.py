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
l = a[0][0]
r = a[0][0]
for i in range(n):
    for j in range(m):
        l = min(l, a[i][j])
        r = max(r, a[i][j])

check = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == r-l:
            if check == 0: print(a[i][j])
            print("Vi tri ["+str(i)+"]["+str(j)+"]")
            check = 1
if check == 0:
    print("NOT FOUND")