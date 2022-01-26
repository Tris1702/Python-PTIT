"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
a = []
while True:
    a.extend(list(int(x) for x in input().split()))
    # print(len(a))
    if len(a) == n: break
a.sort()
check = 0
for i in range(1, max(a)):
    if i not in a:
        print(i)
        check = 1

if check == 0:
    print('Excellent!')