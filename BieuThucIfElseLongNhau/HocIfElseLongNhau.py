dtb = float(input('Nhập điểm trung bình: '))

if dtb > 8:
    print('Xếp loại giỏi!')
elif (dtb > 6) and (dtb <= 8):
    print('Xếp loại khá!')
elif (dtb > 3) and (dtb <= 6):
    print('Xếp loại trung bình')
else:
    print('Xếp loại yếu!')