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

N = int(input())
arr = input().split()
dict = {}
for i in arr:
    if isPrime(int(i)):
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
for key, val in dict.items():
    print(str(key) + ' ' + str(val))