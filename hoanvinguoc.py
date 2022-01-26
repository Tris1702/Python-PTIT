"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
from itertools import permutations
import math

T = int(input())
for t in range(T):
    n = int(input())
    s = ''
    for i in range(1, n+1): s = str(i)+s
    res = permutations(s)
    print(math.factorial(n))
    for i in res:
        print(**i, sep ='', end = ' ')
    