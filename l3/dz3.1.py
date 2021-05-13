def my_func (n1, n2):
    try:
        n3 = n1 / n2
        return n3
    except ZeroDivisionError:
        return "Второе число не может быть нулём"
    except ValueError:
        return "Вводите только числа"
print(my_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))