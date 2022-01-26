"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    la = []
    n, k = map(int, input().split())
    l = list(int(x) for x in input().split())
    maxx = 0
    for i in range(1, n):
        if l[i] > l[maxx]: maxx = i

    l.insert(maxx, k)    
    for i in l:
        if i < 0:
            la.append(i)
    for i in la: print(i, end = ' ')
    for i in l:
        if i >= 0:
            print(i, end = ' ')
    print()