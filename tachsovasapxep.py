"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

N = int(input())
list_num = []
for n in range(N):
    s = input()
    s = s+'#'
    num = -1
    for i in s:
        if i.isnumeric():
            if num == -1:
                num = 0
            num = num * 10 + int(i)
        else:
            if num != -1:
                list_num.append(num)
            num = -1
list_num = sorted(list_num)
for i in list_num:
    print(i)