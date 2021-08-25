"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def checkSumOfDigits(x):
    sum = 0
    for i in x:
        sum = sum + int(i)
    return sum % 10 == 0

def checkDifferenceBetweenTwoDigits(x):
    for i in range(1, len(x)):
        if abs(int(x[i])- int(x[i-1])) != 2:
            return False
    return True

T = int(input())
for t in range(T):
    x = input()
    if checkDifferenceBetweenTwoDigits(x) and checkSumOfDigits(x):
        print('YES')
    else: 
        print('NO')