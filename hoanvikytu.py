"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
from itertools import permutations
s = input()
res = permutations(s)
for i in res:
    print(*i, sep ='')