"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def compress(x):
    count = 0
    while (len(x) > 1):
        count = count + 1
        tmp = 0
        for i in x:
            tmp = tmp + int(i)
        x = str(tmp)
    return count

s = input()
s = s.lstrip('-')
print(compress(s))