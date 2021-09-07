"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = list(str(i) for i in input())
    if len(s) == 1: 
        print(-1)
        continue
    i = len(s)-2
    while i >= 0 and s[i] <= s[i+1]:
        i = i - 1
    if (i < 0):
        print(-1)
    else:
        max = i+1
        for j in range(i+1, len(s)):
            if s[j] < s[i] and s[j] > s[max]:
                max = j
        s[max], s[i] = s[i], s[max]
        if s[0] == '0':
            print(-1)
        else:
            for j in s:
                print(j,end='')
            print()
