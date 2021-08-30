"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
arr = list(int(i) for i in input().split())
count = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            count = count + 1

print(count)