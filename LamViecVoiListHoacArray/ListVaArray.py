# for i in range(10):
#     print('So: ', i + 1)

# Áp dụng vào list hoặc array
arrayStr = []
arrayNum = []
lists = ['So 1', 'So 2', 'So 3', 4, 5, 6]
for i in lists:
    if type(i) == str:
        arrayStr.append(i)
    else:
        arrayNum.append(i)

print('Array String: ', arrayStr)
print('Array Number: ', arrayNum)
