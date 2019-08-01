n = int(input('Nhập n: '))

while n < 1:
    n = int(input('Nhập n: '))

# s = 1 + 2 + 3 + ... + n

s = 0
i = 1
while i <= n:
    s = s + i
    i = i + 1

print(s)
