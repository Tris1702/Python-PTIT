"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

import math

a,b,c,d = map(int, input().split())

x = a*d + b*c
y = b*d

print(str(x//math.gcd(x,y)) + '/'+str(y//math.gcd(x,y)))