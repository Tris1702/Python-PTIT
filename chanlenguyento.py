"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

T = int(input())
evenDigit = ['0', '2', '4', '6', '8']
for t in range(T):
    s = input()
    sum = 0
    check = True
    for i in range(0, len(s)):
        sum += int(s[i])
        if i % 2 == 0:
            if s[i] not in evenDigit:
                check = False
                break
        else:
            if s[i] in evenDigit:
                check = False
                break
    if check and isPrime(sum):
        print('YES')
    else:
        print('NO')