#!/usr/bin/env python3
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def fib_v_1(k):
    n = int(k)
    if n == 1:
        fib_list = [1]
    if n >= 2:
        fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


if __name__ == '__main__':
    print('Введите количество чисел Фибоначчи:')
    num = input()

    if isint(num):
        print('Числа Фибоначчи:')
        print(fib_v_1(num))
    else:
        print('Введеное число не является целым!')