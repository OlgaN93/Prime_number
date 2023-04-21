import math
import time

prime = [2, 3]

n = int(input('Введите число, до которого следует вывести простые числа:\n'))

while n < 2:
    n = int(input('Введите число не меньше двух:\n'))
    print()

if n == 2:
    print('1: 2')
    exit(0)

num_loop = int(input('Введите количество циклов:\n'))
print()
sum_time = 0

for loop in range(num_loop):
    start_time = time.time()
    for num in range(5, n):
        sqrt_num = round(math.sqrt(num))
        for p in prime:
            if p <= sqrt_num:
                if num % p == 0:
                    break
            else:
                prime.append(num)
                break

    exe_time = time.time() - start_time
    sum_time += exe_time

print(sum_time / num_loop) #num == 10000000 - 29 сек
                           #num == 100000000 - 436 сек

