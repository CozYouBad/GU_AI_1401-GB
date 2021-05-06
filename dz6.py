a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        result_km = result_km + a * 0.1
        a = a + 0.1 * a
        result_days += 1
print(f"Вы достигнете требуемых показателей на день", result_days)