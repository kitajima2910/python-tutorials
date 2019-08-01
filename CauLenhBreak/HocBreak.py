while True:
    n = int(input('Nhập n: '))
    print(n, ' là số chẵn' if n % 2 == 0 else ' là số lẻ')
    question = input('Có muốn tiếp tục hay không (c/k): ')
    if question == 'k':
        break


s = 0

for i in range(1, n + 1, 1):
    s = s + i
    if s >= 15:
        break

print(s)