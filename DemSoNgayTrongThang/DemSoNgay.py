month = int(input('Nhập vào tháng: '))
if month in (4, 6, 9, 11):
    print('Có 30 ngày!')
elif month == (2):
    year = int(input('Nhập vào năm: '))
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print('Có 29 ngày!')
    else:
        print('Có 28 ngày!')
elif month in (1, 3, 5, 7, 8, 10, 11, 12):
    print('Có 31 ngày!')
else:
    print('Tháng không hợp lệ!')