"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def gcd(a, b):
    while (a > 0):
        if a < b:
            a, b = b, a
        a = int(a % b)
    return b

N = int(input())
arr = list(int(i) for i in input().split())
arr.sort()
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        a = arr[i]
        b = arr[j]
        if gcd(a, b) == 1:
            print(a, b)