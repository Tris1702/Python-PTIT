"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    x = 0
    for i in range(p, n, p):
        while (i % p == 0):
            x = x + 1
            i = i // p
    print(x)