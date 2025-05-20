temp = [3, 5, None, 10, 15, None, 17, 22, 15, None, 9, 8, 3]
# Фильтруем список, удаляя None
filtered_temp = [t for t in temp if t is not None] #оставляет только числа

# Вычисляем среднее значение
average_temp = sum(filtered_temp) / len(filtered_temp)

print(f"Средняя температура: {average_temp:.2f}")