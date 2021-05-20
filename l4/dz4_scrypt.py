from itertools import count
from itertools import cycle
from math import factorial

def sal():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка: '))
        bonus = int(input('Премия: '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника:  {res}')
    except ValueError:
        return print('NaN')


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)

def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1

def fibo_gen():
    for el in count(1):
        yield factorial(el)