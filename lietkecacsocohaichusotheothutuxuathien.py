"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

s = input()
a = {}
for i in range(1, len(s), 2):
    a[int(s[i-1])*10+int(s[i])] = 1
for i in a.keys():
    print(i, end = ' ')