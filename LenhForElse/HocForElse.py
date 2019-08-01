n = int(input('Nhập n: '))
s = 0
for i in range(5, 10, 1):
    if 4 % n is 1:
        print('Stop...')
        break
    s = s + i
else:
    print(s)