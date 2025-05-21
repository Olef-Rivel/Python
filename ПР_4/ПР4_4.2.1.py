#
# Выполнил: Машук Ю.Н.
# Группа: МС-32

import math

def sgn(x):
    
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

    # Удалите комментарий и допишите код

x = int(input("Enter the number x "))
y = int(input("Enter the number y "))

# Вычисление выражения
z = sgn(x) + (y**2) / (sgn(y) - math.sqrt(abs(x)))

print("Ответ:", z)

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33
