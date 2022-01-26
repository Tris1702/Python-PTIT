"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import re
N = int(input())
for i in range(N):
    l = list(int(x) for x in re.findall('\d+',input()))
    print(sorted(l)[0])