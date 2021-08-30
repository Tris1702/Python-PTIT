"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
N, M = map(int, input().split())
a = list(int(i) for i in input().split())
b = list(int(i) for i in input().split())

A = {}
B = {}
for i in a:
    if i not in A:
        A[i] = 1
for i in b:
    if i not in B:
        B[i] = 1
A = sorted(A.keys())
B = sorted(B.keys())

if A == B:
    print('YES')
else:
    print('NO')