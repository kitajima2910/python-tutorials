import math

toan = float(input('Nhập điểm toán: '))
ly = float(input('Nhập điểm lý: '))
hoa = float(input('Nhập điểm háo: '))

diemTrungBinh = round((toan + ly + hoa) / 3, 2)

print('Điểm trung bình: ', diemTrungBinh)