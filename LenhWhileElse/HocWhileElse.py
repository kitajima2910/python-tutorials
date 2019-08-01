count = sum = 0

while count < 5:
    n = int(input('Nhập n (n >= 0): '))
    if n < 0:
        print('Nhập sai quy tắc...')
        break
    sum = sum + n
    count = count + 1
else:
    print('Trung bình cộng: ', (sum / count))