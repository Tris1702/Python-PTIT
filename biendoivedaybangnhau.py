"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
a = list(int(i) for i in input().split())
minn = 10**9
res = 0
for i in a:
    count = 0
    for j in a:
        count += abs(j-i)
    if count < minn:
        minn = count
        res = i
print(minn, res)
