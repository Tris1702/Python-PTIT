"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
n = int(input())
l = sorted(list(int(x) for x in input().split()))

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if math.gcd(l[i], l[j]) == 1:
            print(l[i], l[j])