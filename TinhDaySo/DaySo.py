x = int(input('Nhập x: '))
n = int(input('Nhập n: '))

s = 0

for i in range(1, n + 1, 1):
    tu = x ** i
    mau = 1
    for j in range(1, i + 1, 1):
        mau = mau * j
    s = s + (tu / mau)
else:
    print('S({0}, {1}) = '.format(x, n), s)