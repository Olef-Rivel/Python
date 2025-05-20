import math

x = int(input("Enter the number x "))
y = int(input("Enter the number y "))

# Функция для вычисления sgn(a)
def sgn(a):

    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

# Вычисление выражения
z = sgn(x) + (y**2) / (sgn(y) - math.sqrt(abs(x)))

# Проверка деления на ноль
if sgn(y) - math.sqrt(abs(x)) == 0:
    print("Ошибка: деление на ноль!")
else:
    print(f"Результат: {z}")