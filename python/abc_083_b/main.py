#桁数を足し合わせる関数
def calc_sum_digits(n):

  sum_digit = 0
  while n > 0:
    sum_digit += n % 10
    n //= 10

  return sum_digit

n, a, b = map(int, input().split())

result = 0

for i in range(1, n + 1):
  if a <= calc_sum_digits(i) <= b:
    print(i)
    result += i

print(result)
