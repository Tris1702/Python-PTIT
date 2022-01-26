"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n,m = map(int, input().split())

maxx = 0
minn = 10001
x = []
for i in range(n):
    l = list(int(x) for x in input().split())
    maxx = max(maxx, max(l))
    minn = min(minn, min(l))
    x.append(l)
dep = maxx - minn
res = []
for i in range(n):
    for j in range(m):
        if x[i][j] == dep:
            res.append([i,j])
            
if len(res) == 0: print('NOT FOUND')
else:
    print(dep)
    for tmp in res:
        print('Vi tri ['+str(tmp[0])+']['+str(tmp[1])+']')    
