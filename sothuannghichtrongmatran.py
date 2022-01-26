"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""
def ispalindrome(x):
    return len(x) >1 and x == x[::-1]

n,m = map(int, input().split())

maxx = -1
x = []
for i in range(n):
    l = list(int(x) for x in input().split())
    for j in l:
        if ispalindrome(str(j)):
            maxx = max(maxx, j)
    x.append(l)
res = []
for i in range(n):
    for j in range(m):
        if x[i][j] == maxx:
            res.append([i,j])
            
if len(res) == 0: print('NOT FOUND')
else:
    print(maxx)
    for tmp in res:
        print('Vi tri ['+str(tmp[0])+']['+str(tmp[1])+']')    
