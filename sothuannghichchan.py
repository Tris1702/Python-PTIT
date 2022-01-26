"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def fullOfEven(x):
    for i in x:
        if int(i) % 2:
            return False
    return True
def mirror(i):
    i = str(i)
    return i+i[::-1]

T = int(input())
for t in range(T):
    N = int(input())
    x = 1
    while True:
        if fullOfEven(str(x)):
            i = mirror(x)
            if int(i) >= N: break
            print(i, end=' ')
        x+=1
    print()