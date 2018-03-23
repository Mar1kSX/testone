#!/usr/bin/env python3

import sys


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


def fact_v_1(k):
    n = int(k)
    if n == 1:
        return 1
    else:
        return n * fact_v_1(n - 1)


def main():
    print(sys.argv[0])
    num_fib = sys.argv[1]
    num_fact = sys.argv[2]

    if isint(num_fib) and isint(num_fact):
        print('Список {}-первых чисел Фибоначчи:'.format(num_fib))
        print(fib_v_1(num_fib))
        print('Факториал числа {}:'.format(num_fact))
        print(fact_v_1(num_fact))
    else:
        print('Ошибка ввода целого числа!')


if __name__ == '__main__':
    main()
