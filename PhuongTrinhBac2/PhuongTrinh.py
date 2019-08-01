from math import *

# ax^2 + bx + c = 0
print('*'*10 + 'GIẢI PHƯƠNG TRÌNH BẬC 2' + '*'*10)
a = float(input('Nhập hệ số a: '))
b = float(input('Nhập hệ số b: '))
c = float(input('Nhập hệ số c: '))

if a == 0:
    if b == 0:
        if c == 0:
            print('Phương trình vô số nghiệm')
        else:
            print('Phương trình vô nghiệm')
    else:
        x = -c / b
        print('Nghiệm x = ', x)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Phương trình vô nghiệm')
    else:
        if delta == 0:
            x = -b / (2 * a)
            print('Nghiệm kép: ', x)
        else:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            print('Nghiệm x1 = {0}, x2 = {1}'.format(x1, x2))
