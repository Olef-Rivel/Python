
# Выполнил: Машук Ю.Н.
# Группа: МС-32



def gcd(first, second):
    """Вернуть НОД целых чисел 'first' и 'second'."""
    while first > 0 and second > 0:
        if first >= second:
            first = first % second
        else:
            second = second % first
    return max(first, second)


def lcm(first, second):
    """Вернуть НОК целых чисел 'first' и 'second'."""
    return (first * second) // gcd(first, second)


def gcd_nums(nums):
    # Вернуть НОД чисел из списка 'nums'. 

    current_gcd = nums[0]
    for i in nums[1:]:
        current_gcd = gcd(current_gcd, i)
    return current_gcd
    
    # Удалите комментарий и допишите код


def lcm_nums(nums):
    """Вернуть НОК чисел из списка 'nums'.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    current_lcm = nums[0]
    for i in nums[1:]:
        current_lcm = lcm(current_lcm, i)
    return current_lcm



nums_str_list = input("Введите числа через пробел: ").split()
nums_int_list = list()

for i in nums_str_list:
    nums_int_list.append(int(i))


print(f"НОД = {gcd_nums(nums_int_list)}")
print(f"НОК = {lcm_nums(nums_int_list)}")
# --------------
# Пример вывода:
#
# Введите числа через пробел: 8 10 14
# НОД = 2
# НОК = 280
#
# Введите числа через пробел: 6 8 24 16
# НОД = 2
# НОК = 48
