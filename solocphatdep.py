"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def check(s):
    if ('888' in s) or (s[0] == '8'):
        return 'NO'
    for i in s:
        if i != '6' and i != '8':
            return 'NO'
    return 'YES'

s = input()
print(check(s))