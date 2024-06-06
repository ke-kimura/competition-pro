a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for a in range(a + 1):
    for b in range(b + 1):
        for c in range(c + 1):
            if 500 * a + 100 * b + 50 * c == x:
                count += 1

print(count)


#リスト内包表記を使うと以下のようになる
# a = int(input())
# b = int(input())

# c = int(input())
# x = int(input())

# print(sum(500 * a + 100 * b + 50 * c == x for a in range(a + 1) for b in range(b + 1) for c in range(c + 1)))
