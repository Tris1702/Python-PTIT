"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def inc(a):
    for i in range(1, len(a)):
        if int(a[i]) <= int(a[i-1]): return i-1
    return len(a)-1

def dec(a, vt):
    if vt == 0 or vt == len(a)-1: return False
    for i in range(vt+1, len(a)):
        if a[i] >= a[i-1]: return False
    return True 

T = int(input())
for t in range(T):
    a = input()
    if len(a) < 3: print('NO')
    else:
        vt = inc(a)
        if dec(a, vt): print('YES')
        else: print('NO')