"""
Author: Tris1702
Github: https://github.com/Tris1702
Gmail: phuonghoand2001@gmail.com
Thank you so much!
"""

n, m = map(int, input().split())
a = list(int(i) for i in input().split())
result = {}
for i in a:
    if i not in result:
        result[i] = 1
    else: result[i] += 1
result = sorted(result.items(), key = lambda x : (x[1], -x[0]), reverse=True)
if result[0][1] == result[-1][1]: print("NONE")
else:
    it = 1
    while (result[it][1] == result[0][1]): it += 1
    print(result[it][0])