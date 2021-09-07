"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def isPalindrome(x):
    s = str(x)
    return x > 10 and s == s[::-1]

n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
maxx = 0
for i in range(n):
    for j in range(m):
        if isPalindrome(a[i][j]):
            maxx = max(a[i][j], maxx)
if maxx == 0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if isPalindrome(a[i][j]) and a[i][j] == maxx:
                print("Vi tri ["+str(i)+"]["+str(j)+"]")

