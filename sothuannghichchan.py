"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def isPalindrome(x):
    x = str(x)
    return x == x[::-1]

def fullOfEven(x):
    x = str(x)
    for i in x:
        if int(i) % 2:
            return False
    return True

def numberOfDigitsIsEvenNumber(x):
    x = str(x)
    return len(x) % 2 == 0
    
T = int(input())
for t in range(T):
    N = int(input())
    for i in range(N):
        if isPalindrome(i) and fullOfEven(i) and numberOfDigitsIsEvenNumber(i):
            print(i, end=' ')
    print()