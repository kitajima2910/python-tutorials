from time import *

startTime = perf_counter()

s = 0
for i in range(1, 1000, 1):
    s = s + i

endTime = perf_counter() - startTime

print(endTime)