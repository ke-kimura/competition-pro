# n = int(input())


# def fizz_buzz_sum(n):

#   # 初期化
#   sum_extra_fizz_buzz = 0

#   #判定処理
#   for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#       continue
#     elif i % 3 == 0:
#       continue
#     elif i % 5 == 0:
#       continue
#     else:
#       sum_extra_fizz_buzz += i

#   return sum_extra_fizz_buzz


# print(fizz_buzz_sum(n))



# これでOKらしい。。。
# pythonは0の場合falseなので、3,5,15で割り切れないものはtrueになりカウントされる。

count = 0
n = int(input())
for i in range(1, n+1):
  if i%3 and i%5:
    count += i
print(count)

# 正直以下の方が可読率はある。

# n = int(input())

# def fizz_buzz_sum(n):
#     # 初期化
#     sum_extra_fizz_buzz = 0

#     # 判定処理
#     for i in range(1, n+1):
#         if i % 3 != 0 and i % 5 != 0:
#             sum_extra_fizz_buzz += i

#     return sum_extra_fizz_buzz

# print(fizz_buzz_sum(n))
