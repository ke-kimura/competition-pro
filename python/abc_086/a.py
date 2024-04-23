# aとbの積が偶数か奇数か判断してください。

a, b = map(int, input().split())
if (a * b) % 2 == 0:
    print('Even')
else:
    print('Odd')
