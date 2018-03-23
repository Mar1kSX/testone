print('Введите количество чисел Фибоначчи:')
num=input()

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def fibV1(k):
    n = int(k)
    if n == 1: fib_list = [1]
    if n >= 2:
        fib_list = [1, 1]
        for i in range(2, n - 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    print(fib_list)

if isint(num):
    print('числа Фибоначчи:')
    fibV1(num)

else: print('Введеное число не является целым')
