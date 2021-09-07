"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = input()
    num = 0
    for i in s:
        num += int(i)
    if num % 3 == 0:
        print('YES')
    else: print('NO')