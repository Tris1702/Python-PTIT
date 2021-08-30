"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

palindrome = []
arr = [0]

def calculate(s):
    sum = 0
    so = 1
    s = s[::-1]
    for i in s:
        if i == '1':
            sum = sum + so
        so = so * 2
    return sum

def prepare(s):
    if len(s)>21:
        return
    if len(s) > 0 and s[0] != '0':
        palindrome.append(calculate(s))
    prepare('0'+s+'0')
    prepare('1'+s+'1')

def BS(l, r, x):
    while l <= r:
        mid = (l+r)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid]>x:
            r = mid-1
        else:
            return mid
    return -1

l, r, n = map(int, input().split())

if n==3:
    res = 0
    if l == 0: res = res + 1
    if l <= 1 and 1 <= r:
        res = res + 1
    if (l<=6643 and 6643<=r):
        res = res + 1
    if l <= 1422773 and 1422773 <= r:
        res = res + 1
    print(res)
if n>3:
    res = 0
    if l == 0: 
        res= res+1
    if l<= 1 and 1<= r:
        res = res + 1
    print(res)
if n == 2:
    dem = 0
    prepare('')
    prepare('1')
    prepare('0')
    palindrome.sort()
    palindrome.append(0)
    for i in range(0, len(palindrome)-1):
        if palindrome[i] != palindrome[i+1]:
            arr.append(palindrome[i])
    offset = 0
    if BS(0, len(arr)-1, l) == -1:
        arr.append(l)
        offset = offset + 1
    if BS(0, len(arr)-1, r) == -1:
        arr.append(r)
        offset = offset + 1
    arr.sort()
    it1 = BS(0, len(arr)-1, l)
    it2 = BS(0, len(arr)-1, r)
    print(it2 - it1 + 1 - offset)