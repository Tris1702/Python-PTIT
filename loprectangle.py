"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

class Rectangle:
    def __init__(self, h, w, c):
        self.h = h
        self.w = w
        self.c = c
    def perimeter(self):
        return 2*(self.h+self.w)
    def area(self):
        return self.h * self.w
    def color(self):
        return self.c.title()
    def isvalid(self):
        return self.h > 0 and self.w > 0

arr = input().strip().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.isvalid():
    print(r.perimeter(), r.area(), r.color())
else: print('INVALID')