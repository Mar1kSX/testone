#!/usr/bin/env python3

import sys


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


class MyMath:
    """
    init class
    """
    def __init__(self):
        pass

    def fib(self, k):
        """
        Some description...
        :param k:
        :return: Fibonachi's list of numbers
        """
        n = int(k)
        if n == 1:
            fib_list = [1]
        if n >= 2:
            fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list

    def fact(self, k):
        """
        Some description...
        :param k:
        :return: factorial of number
        """
        n = int(k)
        if n == 1:
            return 1
        else:
            return n * self.fact(n - 1)


def main():
    num_fib = sys.argv[1]
    num_fact = sys.argv[2]

    if isint(num_fib) and isint(num_fact):
        mymath = MyMath()
        print('Список {}-первых чисел Фибоначчи:'.format(num_fib))
        print(mymath.fib(num_fib))
        print('Факториал числа {}:'.format(num_fact))
        print(mymath.fact(num_fact))
    else:
        print('Ошибка ввода целого числа!')


if __name__ == '__main__':
    main()
