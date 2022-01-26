"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    n, d = map(int, input().split())
    l = input().split()
    vt = d%n
    for i in range(vt, n):
        print(l[i], end = ' ')
    for i in range(d):
        print(l[i], end = ' ')
    print()