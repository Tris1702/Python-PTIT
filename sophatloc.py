"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
T = int(input())
for t in range(0, T):
    s = input()
    sl = len(s)
    if sl >=2 and s[sl-2] == '8' and s[sl-1] =='6':
        print('YES')
    else:
        print('NO')