result = 0
while True:
    line = input('Введите число или f для выхода: ')
    numbers = line.split(' ')
    for number in numbers:
        try:
            numb = float(number)
            result += numb
            print(f'Сумма: {result}')
        except:
            if number == 'f':
                print(f'Сумма: {result}. Выход...')
                exit(0)
            else:
                print(f'Сумма: {result}. Ошибка ввода')
                exit(0)