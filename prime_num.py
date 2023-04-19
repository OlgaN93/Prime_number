import math

prime = [2, 3]

n = int(input('Введите число, до которого следует вывести простые числа:\n'))
print()

while n < 2:
    n = int(input('Введите число не меньше двух:\n'))
    print()

if n == 2:
    print('1: 2')
    exit(0)

for num in range(5, n + 1):
    sqrt_num = round(math.sqrt(num))
    for p in prime:
        if p <= sqrt_num:
            if num % p == 0:
                break
        else:
            prime.append(num)
            break

i = 1
for num in prime:
    print(i, num, sep=': ')
    i += 1
