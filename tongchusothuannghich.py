"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def isPalindrome(x):
    s = str(x)
    if len(s) > 1 and s == s[::-1]:
        return 'YES'
    else:
        return 'NO'

T = int(input())
for t in range(T):
    s = input()
    num = 0
    for i in s:
        num += int(i)
    print(isPalindrome(num))