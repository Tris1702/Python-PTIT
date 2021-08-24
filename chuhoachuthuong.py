"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
s = input()
dem = 0
for i in s:
    if i.islower():
        dem = dem+1
if dem >= len(s)-dem:
    print(s.lower())
else:
    print(s.upper())
