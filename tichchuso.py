"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    s = input()
    num = 1
    for i in s:
        if i != '0':
            num *= int(i)
    print(num)