# Из десятичной
def to_base_n(number, base):
    digits = "0123456789ABCDEF"  # Поддержка систем до 16-ричной
    result = ""
    
    while number > 0:
        result = digits[number % base] + result
        number //= base
    
    return result if result else "0"  # Если число 0, возвращаем "0"

# Пример использования:
num = int(input("Введите число в 10-й системе: "))
base = int(input("Введите систему счисления (2-16): "))

print(f"{num} в системе {base}: {to_base_n(num, base)}")

# В десятиричну

def from_base_n(number_str, base):
    return int(number_str, base)

# Пример использования:
num_str = input("Введите число в N-й системе: ")
base = int(input("Введите систему счисления (2-16): "))

print(f"{num_str} из системы {base} в 10-й: {from_base_n(num_str, base)}")
