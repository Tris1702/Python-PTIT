"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n = int(input())
for i in range(n):
    dd, mm = map(int, input().split())

    if mm == 1:
        if dd >= 20: print('Bao Binh')
        else: print('Ma Ket')
    
    if mm == 2:
        if dd >= 19: print('Song Ngu')
        else: print('Bao Binh')

    if mm == 3:
        if dd >= 21: print('Bach Duong')
        else: print('Song Ngu')
    
    if mm == 4:
        if dd >=20: print('Kim Nguu')
        else: print('Bach Duong')
    
    if mm == 5:
        if dd >=21: print('Song Tu')
        else: print('Kim Nguu')
    if mm == 6:
        if dd >=21: print('Cu Giai')
        else: print('Song Tu')
    
    if mm == 7:
        if dd >=23: print('Su Tu')
        else: print('Cu Giai')
    
    if mm == 8:
        if dd >=23: print('Xu Nu')
        else: print('Su Tu')

    if mm == 9:
        if dd >=23: print('Thien Binh')
        else: print('Xu Nu')

    if mm == 10:
        if dd >=23: print('Thien Yet')
        else: print('Thien Binh')

    if mm == 11:
        if dd >=23: print('Nhan Ma')
        else: print('Thien Yet')

    if mm == 12:
        if dd >=22: print('Ma Ket')
        else: print('Nhan Ma')
    