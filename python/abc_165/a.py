k = input()
k = int(k)
a, b = map(int, input().split())

x = "NG"

for i in range(a, b + 1):
    if i % k == 0:
      x = "OK"
      break

print(x)
