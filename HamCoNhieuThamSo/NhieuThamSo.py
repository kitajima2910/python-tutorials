def soTuNhien(a, b, *num):
    print('A: ', a)
    print('B: ', b)
    for i in num:
        print('- ', i)

soTuNhien(5, 6, 1, 2, 3, 4, 5)

def soTuNhienClone():
    x = 5
    y = 6
    return [x, y]

print('Result: ', soTuNhienClone()[0] + soTuNhienClone()[1])