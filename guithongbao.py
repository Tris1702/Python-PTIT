"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = input()
    nt = s[:min(len(s), 100)]
    if len(nt) == 100:
        x = nt.split()
        xx = s.split()
        if x[-1] != xx[len(x)-1]:
            while nt[-1]!= ' ': nt = nt[:-1]
    print(nt)