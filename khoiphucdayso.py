"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
arr = []
for i in range(n):
    arr.append(list(int(i) for i in input().split()))

if (n == 2):
    print(n//2, n//2)
else:
    # find the first number
    sum1 = 0
    for i in range(n):
        if i == n-1:
            sum1 = sum1 + arr[i][0] 
        else: sum1 = sum1 + arr[i][i+1]
    sum2 = 0
    for i in range(1, n):
        if i == n-1:
            sum2 = sum2 + arr[i][1] 
        else: sum2 = sum2 + arr[i][i+1]
    res = [(sum1-sum2)//2]
    # find the other
    for i in range(1, n):
        res.append(arr[i-1][i] - res[len(res)-1])
    for i in res:
        print(i, end = ' ')