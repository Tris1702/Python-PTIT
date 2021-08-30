"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def compress(s):
    s1 = ''
    s2 = ''
    for i in range(0, len(s)//2):
        s1 = s1 + s[i]
    for i in range(len(s)//2, len(s)):
        s2 = s2 + s[i]
    return str(int(s1) + int(s2))
s = input()
while len(s) > 1:
    s = compress(s)
    print(s)