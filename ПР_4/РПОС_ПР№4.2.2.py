# Выполнил: Машук Ю.Н.
# Группа: МС-32



def avg(data):
    average_value = 0.0
    n = len(data)
    for i in data:
        average_value += i / n

    return average_value


def cleared_data(data):
    for i in data:
        if i == None:
            data.remove(i)
    return data


n = int(input("Кол-во измерений: "))

data = list()
for i in range(n):
    value = input(f"Измерение {i+1}-е: ")
    if value == '-':
        data.append(None)
    elif value.isdigit():
        data.append(float(value))


average_value = avg(cleared_data(data))
print(f"Средняя температура: {average_value}")

# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.00
