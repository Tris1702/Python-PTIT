"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

def gia(loai, sl):
    if loai == 'Xe_con':
        if sl == '5': return 10000
        else: return 15000
    if loai == 'Xe_tai': return 20000
    if loai == 'Xe_khach':
        if sl == '29': return 50000
        else: return 70000

n = int(input())
ngay = {}
for i in range(n):
    xe = input().split()
    if xe[3] == 'IN':
        if xe[4] not in ngay:
            ngay[xe[4]] = gia(xe[1], xe[2])
        else: 
            ngay[xe[4]] += gia(xe[1], xe[2])
d = sorted(ngay.items(), key=lambda x: x[0])
for i in d:
    print(str(i[0])+':',i[1])