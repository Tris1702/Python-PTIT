"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
s = input()[::-1]
res =''
for i in range(0, len(s)):
    res = s[i] + res
    if i % 3 == 2:
        res = ',' + res

print(res.lstrip(','))