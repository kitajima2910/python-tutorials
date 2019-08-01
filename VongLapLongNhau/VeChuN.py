n = int(input('Nhập n: '))

# for i in range(0, n, 1):
#     for j in range(0, n, 1):
#         if j is 0 or i is j or j is n - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

i = 0
while i < n:
    j = 0
    while j < n:
        if j is 0 or i is j or j is n - 1:
            print('$', end='')
        else:
            print(' ', end='')
        j = j + 1
    i = i + 1
    print()