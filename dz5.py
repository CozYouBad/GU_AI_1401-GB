profit = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")