"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

class Student:
    def __init__(self, name, dob, score1, score2, score3):
        self.name = name
        self.dob = dob
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def show(self):
        print(self.name, self.dob, format((self.score1+self.score2+self.score3),'.1f'))
    
st = Student(input(), input(), float(input()), float(input()), float(input()))
st.show()