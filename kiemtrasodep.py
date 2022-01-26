"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def isPretty(a):
    for i in range(2, len(a), 2):
        if (a[i] != a[0]): return False
    for i in range(3, len(a), 2):
        if (a[i] != a[1]): return False
    return True
T = int(input())
for t in range(T):
    if isPretty(input()): print('YES')
    else: print('NO') 