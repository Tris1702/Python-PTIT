"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1

n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
maxx = 0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            maxx = max(a[i][j], maxx)
if maxx == 0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if isPrime(a[i][j]) and a[i][j] == maxx:
                print("Vi tri ["+str(i)+"]["+str(j)+"]")

