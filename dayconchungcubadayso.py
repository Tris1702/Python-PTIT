"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def solve():
    n1, n2, n3 = map(int, input().split())
    a = list(int(x) for x in input().split())
    b = list(int(x) for x in input().split())
    c = list(int(x) for x in input().split())
    i = 0
    j = 0
    k = 0
    check = True
    while i < n1 and j < n2 and k < n3:
        if a[i] == b[j] and b[j] == c[k]:
            print(a[i], end = ' ')
            check = False
            i = i + 1
            j = j + 1
            k = k + 1
            continue
        if a[i] < b[j] or a[i] < c[k]: 
            i = i + 1
            continue
        if b[j] < c[k] or b[j]<a[i]: 
            j = j + 1
            continue
        if c[k] < a[i] or c[k] < b[j]: 
            k = k + 1
            continue
    if check: print('NO',end = ' ')
    print()
T = int(input())
for t in range(T):
    solve()
