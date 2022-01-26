"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

l=[]
dem = 0
n = int(input())
for i in range(n):
    x = input()
    if x not in l:
        l.append(x)
        dem += 1
print(dem)