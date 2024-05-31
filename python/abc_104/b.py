# Check関数
def acCheck(s):

  if s[0] != "A":
    return "WA"

  if s[2:-1].count("C")!= 1:
    return "WA"

  if sum(map(str.isupper, s))!= 2:
      return "WA"

  return "AC"

# Input
s = input()
# Output
print(acCheck(s))
