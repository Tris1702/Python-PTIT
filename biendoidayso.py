"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def allEqual(a):
    return a[0] == a[1] and a[1] == a[2] and a[2] == a[3]

while True:
    arr = list(int(i) for i in input().split())
    if arr[0] == 0 and allEqual(arr):
        break
    count = 0
    while allEqual(arr) == False:
        count = count + 1
        tmp = arr[0]
        arr[0] = abs(arr[0] - arr[1])
        arr[1] = abs(arr[1] - arr[2])
        arr[2] = abs(arr[2] - arr[3])
        arr[3] = abs(arr[3] - tmp)
        # print(arr)
    print(count)