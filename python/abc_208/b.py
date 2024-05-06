p = int(input())

ans = 0

import math

for i in range (10, 0, -1):
  # i!円のコイン
  coin = math.factorial(i)

  while coin <= p:
    ans += 1
    p -= coin

print(ans)
