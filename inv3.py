A = int(input('Введите число: '))

for d in range(1, A // 2 + 1):
    if A % d == 0:
        print(d, ' ', sep='', end='')
print(A)