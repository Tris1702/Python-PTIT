"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

N = int(input())
i = 0
tl = -1
res =[]
dem = 0
while i < N:
    line = input().split()
    if len(line) == 7 and (dem == 4 or tl != 2):
        if dem == 4: dem = 0
        tl = 2
        res.append(tl)
    elif (len(line) == 6 or len(line) == 8) and tl != 1:
        tl = 1
        dem = 0
        res.append(tl)
    if tl == 2: dem+=1
    i += 1
print(len(res))
for i in res:
    print(i)
    