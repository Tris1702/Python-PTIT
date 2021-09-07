def bai1():
    a = list(int(i) for i in input().split())
    # xoa phan tu cuoi
    a.pop()
    print(a)
    # Chen
    a.insert(3, 10)
    print(a)
    # Doi gia tri
    a[0] = 'Python'
    print(a)

def bai2():
    a = list(int(i) for i in input().split())
    # swap
    t = a[0]
    a[0] = a[-1]
    a[-1] = t
    print(a)

def bai3():
    a = list(int(i) for i in input().split())
    b = list(i for i in a if i%2 != 0)
    # b =[]
    # for i in a:
    #     if i %2 != 0: b.append(i)
    print(b)

def bai4():
    a = input().split()
    sum = 0
    sl = 0
    for i in a:
        if i.isnumeric():
            sum += int(i)
            sl += 1
    print(sum, sum//sl)

def bai5():
    a = [4, 2, 3, 1, 4, 6, 4]
    for i in range(0, len(a)):
        a[i] *= a[i]
    print(sorted(a, reverse= True))
def bai6():
    a = [1, 'a', 34, 'a', 'b', 1, 'c']
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(len(b))

bai5()
bai6()