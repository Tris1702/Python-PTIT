"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

N = int(input())
arr = [0]
for i in input().split():
    arr.append(int(i))
arr.append(300000)
arr.sort()
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        continue
    if arr[i] != arr[i-1]+1:
        print(arr[i-1]+1) 
        break   