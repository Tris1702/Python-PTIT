"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def decToOct(x):
    switcher = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7'
    }
    return switcher.get(x, '')

s = input()
while len(s) % 3:
    s = '0'+s
res = ''
for i in range(0, len(s), 3):
    tmp = s[i] + s[i+1] + s[i+2]
    res = res + decToOct(tmp)
print(res)