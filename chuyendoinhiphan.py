"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def w(so):
    if so < 10: return str(so)
    if so == 10: return 'A'
    if so == 11: return 'B'
    if so == 12: return 'C'
    if so == 13: return 'D'
    if so == 14: return 'E'
    if so == 15: return 'F'


def doi(s, sl):
    while len(s) % sl != 0: s = '0'+s
    res = ''
    for i in range(len(s)-1, 0, -sl):
        x = 1
        so = 0
        for j in range(i, i-sl, -1):
            if j >= 0:
                so += x*int(s[j])
                x *= 2
        res = res + w(so)
    return res[::-1]

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    s = input().strip()
    if N == 2:
        print(s)
    elif N == 4:
        print(doi(s, 2))
    elif N == 8:
        print(doi(s, 3))
    else: print(doi(s, 4))