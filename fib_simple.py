print('Введите количество чисел Фибоначчи:')
num=input()

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

if isint(num):
    n=int(num)
    if n == 1: fib_list = [1]
    if n >= 2:
        fib_list = [1, 1]
        i = 2
        while i <= n - 1:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
            i += 1
        print('числа Фибоначчи:')
        print(fib_list)

else: print('Введеное число не является целым')