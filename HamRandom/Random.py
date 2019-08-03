from random import *

count = 0
while True:
    x = randrange(-5, 6)
    count = count + 1
    print(x, end='|')
    if x is 0:
        break

print('Bye bye!... = ', count)