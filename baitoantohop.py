"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
from itertools import combinations

n,k = map(int, input().split())
l = list(set(int(x) for x in input().split()))
l.sort()
res = combinations(l,k)
for i in res:
    print(*i)