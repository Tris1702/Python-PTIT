"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def ktr(s):
    if len(s) % 2 == 0 or s[0] == s[1]: return 'NO'
    for i in range(0, len(s), 2):
        if s[i] != s[0]: return 'NO'
    return 'YES'
T = int(input())
for t in range(T):
    s = input()
    print(ktr(s))