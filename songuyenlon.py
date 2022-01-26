"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

t = int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    print(b)