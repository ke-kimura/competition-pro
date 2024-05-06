n = int(input())
a = int(input())

remainder = n % 500

if n >= 500 and remainder == 0 :
  print("Yes")
elif n < 500:
  if (n - a) <= 0:
    print("Yes")
  else:
    print("No")
else:
  if (remainder - a) <= 0:
    print("Yes")
  else:
    print("No")
