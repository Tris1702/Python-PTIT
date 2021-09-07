"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math

def gcd(a, b):
    while (a > 0):
        if a < b:
            a, b = b, a
        a %= b
    return b

a, b = map(int,input().split())
l = []
for i in range(a, b-1):
    for j in range (i+1, b):
        if gcd(i, j) == 1:
            l.append([i, j])
for coup in l:
    for i in range(coup[1]+1, b+1):
        if (gcd(i, coup[0])==1) and (gcd(i, coup[1]) == 1):
            print('(' + str(coup[0]) + ', ' + str(coup[1])+', ' + str(i) + ')')