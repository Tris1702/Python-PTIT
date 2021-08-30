"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = list(int(i) for i in input())
    for i in range(len(s)-1, 0, -1):
        if s[i] >= 5:
            s[i-1] = s[i-1] + 1
        s[i] = 0
    if s[0] == 10:
        s[0] = 0
        print(1, end='')
    for i in s:
        print(i, end = '')
    print()