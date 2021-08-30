"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    N = int(input())
    arr = [int(i) for i in input().split()]
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    maxx = 0
    res = 0
    for key, val in dict.items():
        if val > maxx:
            maxx = val
            res = key
    # print(int(N/2))
    if (maxx > int(N/2)):
        print(res)
    else:
        print('NO')
    