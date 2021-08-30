"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def greater(x, y):
    if len(x) > len(y):
        return True
    elif len(x) < len(y):
        return False
    else:
        return x > y

while True:
    N = int(input())
    if N == 0:
        break
    resMax = '0'
    resMin = ''
    for i in range(N):
        x = input()
        while x[0] == '0':
            x = x.lstrip('0')
        if (greater(x, resMax)):
            resMax = x
        if (len(resMin) == 0) or (greater(resMin, x)):
            resMin = x
    if (resMax == resMin):
        print('BANG NHAU')
    else:
        print(resMin + ' ' + resMax)