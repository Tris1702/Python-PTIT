"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())

for t in range(T):
    s = input()
    sum = 0
    pro = 1
    count0 = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if s[i] != '0':
                pro *= int(s[i])
            else: count0 += 1
    if count0 == len(s)//2:
        pro = 0
    print(sum, pro)