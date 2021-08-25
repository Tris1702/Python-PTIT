"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

s1 = input()
s2 = input()
vt = int(input()) - 1
check = True
for i in range(0, len(s1)):
    if (i == vt):
        print(s2, end = '')
        check = False
    print(s1[i], end = '')
if check: print(s2)