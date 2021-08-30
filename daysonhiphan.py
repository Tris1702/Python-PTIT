"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

N = int(input())
arr = list(int(i) for i in input().split())
count = 0
for  i in range(1, N):
    if (arr[i] != arr[i-1]):
        count = count + 1
print(count)