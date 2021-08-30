"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = input()
    s = s + '#'
    count = 1
    res = ''
    for i in range(1, len(s)):
        if (s[i] == s[i-1]):
            count = count + 1
        else:
            res = res + str(count) + s[i-1]
            count = 1
    print(res)