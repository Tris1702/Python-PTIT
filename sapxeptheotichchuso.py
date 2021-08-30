"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def productOfDigits(x):
    pro = 1
    for i in x:
        pro = pro * int(i)
    return pro

T = int(input())
for t in range(T):
    N = int(input())
    arr = input().split()
    dict = {}
    for x in arr:
        i = int(x)
        dict[i] = productOfDigits(x)
    sorted_dict = sorted(dict.items(), key = lambda x: (x[1], x[0])) #x : x[1] theo value, x : x[0] theo key 

    for i in sorted_dict:
        print(i[0], end = ' ')
    print()