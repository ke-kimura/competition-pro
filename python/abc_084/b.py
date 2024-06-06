# a, b = map(int, input().split())
# s = input()

# print("Yes" if s[:a].isdigit() and s[a] == "-" and s[a+1:].isdigit() else "No")

# 正規表現使った方法
import re
a, b = map(int, input().split())
s = input()

if re.match(r"\d{" + str(a) + r"}-\d{" + str(b) + r"}", s):
    print("Yes")
else:
    print("No")
