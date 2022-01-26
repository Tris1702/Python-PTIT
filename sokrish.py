"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def gt(x):
    s = 1
    for i in range(2, x+1):
        s *= i
    return s

T = int(input())
for t in range(T):
    n = input()
    sum = 0
    for i in n:
        sum += gt(int(i))
    print('Yes' if sum == int(n) else 'No')