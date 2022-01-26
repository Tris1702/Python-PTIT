"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def isIPAddress(x):
    if len(x) != 4: return False
    for i in x:
        if i.isdecimal():
            if int(i) < 0 or int(i) > 255: return False
        else: return False
    return True 
T = int(input())

for t in range(T):
    if isIPAddress(input().split('.')): print('YES')
    else: print('NO')
    