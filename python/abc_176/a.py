import math
n, x ,t = map(int, input().split())

need_count = math.ceil(n / x)
print(t * need_count)
