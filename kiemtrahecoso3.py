"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2': return False
    return True 

n = int(input())
for i in range(n):
    if check(input()): print('YES')
    else: print('NO')
