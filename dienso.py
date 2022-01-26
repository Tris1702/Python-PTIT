"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())

for t in range(T):
    n = int(input())
    l = list(set(int(x) for x in input().split()))
    res = 0
    for i in range(1,len(l)):
        if l[i] > l[i-1]+1:
            res += l[i] - l[i-1] - 1
    print(res)