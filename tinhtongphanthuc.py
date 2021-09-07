"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    n = int(input())
    sum = 0.0
    for i in range(2 - n%2, n+1, 2):
        sum += 1.0/i
    print('{:.6f}'.format(sum))