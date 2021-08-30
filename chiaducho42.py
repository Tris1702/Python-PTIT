"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
r = []
count = 0
while (input()):
    for i in input().split():
        so = int(i) % 42
        if (so in r) == False:
            r.append(so)
print(len(r))