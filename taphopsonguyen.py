"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def diff(x):
    res = {}
    for i in x:
        if i not in res:
            res[i] = 1
    return sorted(res.keys())

N, M = map(int, input().split())

a = list(int(i) for i in input().split())
b = list(int(i) for i in input().split())

a = diff(a)
b = diff(b)
res1 = []
res2 = []
res3 = []
for i in a:
    if i in b:
        res1.append(i)
for i in a:
    if i not in res1:
        res2.append(i)
for i in b:
    if i not in res1:
        res3.append(i)
for i in res1:
    print(i, end=' ')
print()
for i in res2:
    print(i, end=' ')
print()
for i in res3:
    print(i, end=' ')
print()