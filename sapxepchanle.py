"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

N = int(input())
le = []
chan = []
sl = 0
arr = []
while sl < N:
    arrtmp = list(int(i) for i in input().split())
    for so in arrtmp:
        sl = sl + 1
        if so % 2 != 0:
            le.append(so)
        else:
            chan.append(so)
    arr.extend(arrtmp)
le.sort(reverse=True)
chan.sort()
i = 0
j = 0
for x in arr:
    if x % 2 != 0:
        print(le[i], end = ' ')
        i = i + 1
    else:
        print(chan[j], end =' ')
        j = j + 1
print()