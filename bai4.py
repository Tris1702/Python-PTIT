s = '''Hello
Xin chao
Hola
Konichiwa'''
s1 = s.split('\n')

max = s1[0]
min = s1[0]
for i in s1:
    if len(max) < len(i):
        max = i
    if len(min) > len(i):
        min = i
print(max, min)
