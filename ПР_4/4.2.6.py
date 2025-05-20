import math
from functools import reduce

# Ввод списка чисел
numbers = list(map(int, input("Введите числа через пробел: ").split()))

# Функция для вычисления НОД
def gcd_list(lst):
    return reduce(math.gcd, lst)

# Функция для вычисления НОК
def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_list(lst):
    return reduce(lcm, lst)

# Вычисление и вывод результатов
print(f"НОД: {gcd_list(numbers)}")
print(f"НОК: {lcm_list(numbers)}")
