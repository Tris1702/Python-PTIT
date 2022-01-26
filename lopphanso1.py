"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

import math

def rutgon(a, b):
    return (a//math.gcd(a,b), b//math.gcd(a,b))

a, b= map(int, input().split())
res = rutgon(a,b)
print(str(res[0]) + '/' + str(res[1]))