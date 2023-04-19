import math
from datetime import datetime

prime = [2, 3]

n = int(input('Введите число, до которого следует вывести простые числа:\n'))
start_time = datetime.now()
if n < 2:
    print('Введите число не меньше двух:\n')
    exit(0)

if n == 2:
    print('1: 2')
    exit(0)

for num in range(5, n):
    sqrt_num = round(math.sqrt(num))
    for p in prime:
        if p <= sqrt_num:
            if num % p == 0:
                break
        else:
            prime.append(num)
            break

print(datetime.now() - start_time) #num == 10000000 - 20 сек



