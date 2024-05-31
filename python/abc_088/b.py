n = int(input())
a = list(map(int, input().split()))

print(a)
sort_a = sorted(a, reverse=True)

alice = 0
bob = 0

for i in range(len(sort_a)):
  if i % 2 == 0:
    alice += sort_a[i]
  else:
    bob += sort_a[i]

print(alice - bob)
