print('Nhập số năm: ')
year = int(input())
result = 'Năm nhuận' if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) else 'Không là năm nhuận'
print(result)
