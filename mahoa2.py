"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    s = input().split()
    k = int(s[0])
    if k == 0:
        break
    s = s[1]
    res = ''
    for i in s:
        pos = p.find(i)
        res = p[(pos + k) % 28] + res
    print(res)