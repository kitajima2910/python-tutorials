while True:
    str = input('Nhập: ')
    if str in ('b', 'bye', '0'):
        exit()
    if str in ['wow']:
        break
    print(str)

print('Hello Exit()')