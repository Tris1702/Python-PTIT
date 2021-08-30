"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = input()
    res = ''
    count = 0
    for i in s:
        if i.isnumeric():
            count = count + int(i)
        else:
            res = res + i
    res = ''.join(sorted(res))
    print(res+str(count))