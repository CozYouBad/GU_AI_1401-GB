def my_func(n1, n2, n3):
    numbers = [n1, n2, n3]
    total = []
    max1 = max(numbers)
    total.append(max1)
    numbers.remove(max1)
    max2 = max(numbers)
    total.append(max2)
    numbers.remove(max2)
    print(sum(total))
my_func(1, 7, 4)