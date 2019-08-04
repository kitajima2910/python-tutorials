def checkString(str):
    flag = True
    for i in range(0, len(str), 1):
        if str[i] is not str[len(str) - i - 1]:
            flag = False
    return flag

while True:
    str = input('Nhập str: ')
    if checkString(str):
        print(str, ' là chuỗi đối xứng...')
    else:
        print(str, ' không là chuỗi đối xứng...')
    key = input('Bạn có muốn tiếp không (Y/N): ')
    if key is ('n'):
        break