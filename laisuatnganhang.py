"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

T = int(input())
for t in range(T):
    N, X, M = input().split()
    N, X, M = float(N), float(X), float(M)
    days = 0
    while (N < M):
        days = days + 1
        N = N + N*(X/100.0)
    print(days)