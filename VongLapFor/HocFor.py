n = int(input('Nhập n: '))

s = 0

if n % 2 == 0:
    for i in range(0, n + 1, 2):
        s = s + i
else:
    for i in range(1, n + 1, 2):
        s = s + i

print(s)