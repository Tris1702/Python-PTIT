"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
while True:
    N = int(input())
    if N == 0: 
        break
    count = {N: 1}
    while N != 1:
        if N%2 == 0:
            N = int(N/2)
        else:
            N = N*3 + 1
        if N not in count:
            count[N] = 1
    print(len(count))