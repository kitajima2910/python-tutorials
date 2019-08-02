n = int(input('Nhập n: '))

count = 0

for i in range(1, n + 1, 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print('Là số nguyên tố')
else:
    print('Không là số nguyên tố')
