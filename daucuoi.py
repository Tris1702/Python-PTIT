"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
T = int(input())
for t in range(T):
    so = input()
    length = len(so)
    if length >=4 and so[0] == so[length-2] and so[1] == so[length-1]:
        print('YES')
    else:
        print('NO')