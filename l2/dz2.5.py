my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
rate = int(input('Введите число (1234, чтобы выйти) '))
while rate != 1234:
    for el in range(len(my_list)):
        if my_list[el] == rate:
            my_list.insert(el + 1, rate)
            break
        elif my_list[0] < rate:
            my_list.insert(0, rate)
        elif my_list[-1] > rate:
            my_list.append(rate)
        elif my_list[el] > rate and my_list[el + 1] < rate:
            my_list.insert(el + 1, rate)
    print(f'текущий список - {my_list}')
    rate = int(input('Введите число '))