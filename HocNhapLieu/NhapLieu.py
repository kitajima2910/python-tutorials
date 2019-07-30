def strToBool(s):
    return s.lower() in ('true', 't', '1', 'yes')


x = input('Mời bạn nhập giá trị: ')
x = strToBool(x)
print("Bạn đã nhập: ", x)
print(type(x))
