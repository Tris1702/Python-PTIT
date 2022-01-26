"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
import re
str = ''
while True:
    try:
        str += input()
    except EOFError:
        break
str = re.split('[.?!]', str)
for i in str:
    if len(i) > 0:
        x = re.sub('\s+',' ',i.strip())
        print(x[0].upper()+x[1:].lower())