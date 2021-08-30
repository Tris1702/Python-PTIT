"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
T = int(input())
for t in range(1, T+1):
    s1 = input()
    s2 = input()
    print('Test '+str(t)+': ', end = '')
    if (len(s1) != len(s2)):
        print('NO')
        continue
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        print('YES')
    else:
        print('NO')