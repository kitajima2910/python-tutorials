import math
try:
    r = float(input('Nhập bán kính r: '))
    cv = math.pi * 2 * r
    dt = math.pi * math.pow(r, 2)

    print('Chu vi hình tròn: ', cv)
    print('Diện tích hình tròn: ', dt)
except:
    print('Lỗi rồi...')