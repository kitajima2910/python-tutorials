n = 15
s = 0
for i in range(1, n + 1, 2):
    if i in [3, 11]:
        continue
    s = s + i

print(s)