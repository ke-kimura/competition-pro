### 回答1 ###

# n = int(input())
# a = list(map(int, input().split()))

# counter = 0

# while True:
#   can_do = True
#   for i in range(n):
#     if a[i] % 2 == 1:
#       can_do = False

#   if not can_do:
#     break

#   for i in range(n):
#     a[i] //= 2
#     print(a[i])

#   counter += 1

# print(counter)

### 回答2 ###
#全ての要素が2で割り切れるかどうかの判定
#配列の全ての要素に対して2で割るなどの処理ができるやり方なので、コード量が少ない

# N = int(input())
# A = list(map(int, input().split()))

# counter = 0

# while all(a % 2 == 0 for a in A):
#   A = [a // 2 for a in A]

#   counter += 1

# print(counter)


### 回答3 ###
#min関数を使うことでもっとシンプルに

def how_many_times(num):
  counter = 0

  while num % 2 == 0:
    num //= 2
    counter += 1
  return counter

N = int(input())
A = list(map(int, input().split()))

result = min(map(how_many_times, A))
# mpaオブジェクトの中身
#result = min(map(how_many_times, A))

print(result)
