"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
""" 
T = int(input())
for t in range(T):
    n = int(input())
    count = {}
    for i in range(n):
        x = int(input())
        if x in count:
            count[x] = count[x] - 1
        else:
            count[x] = -1
    sorted_count = sorted(count.items(), key = lambda x : (x[1], x[0]))
    print(sorted_count[0][0])
