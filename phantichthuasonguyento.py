"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
T = int(input())

for t in range(T):
    x = int(input())
    print('1 ', end = '')
    for i in range(2, int(math.sqrt(x))+1):
        count = 0
        while x % i == 0:
            x = x/i
            count = count + 1
        if count > 0:
            print('* '+str(i)+'^'+str(count)+' ', end = '')
    if x > 1:
        print('* '+str(int(x))+'^1'+' ', end = '')
    print()
