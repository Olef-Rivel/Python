# Ввод границ диапазона
a = int(input("Введите начало диапазона (a): "))
b = int(input("Введите конец диапазона (b): "))

# Перебираем все числа от a до b
for ticket in range(a, b + 1):
    even_count = sum(1 for digit in str(ticket) if int(digit) % 2 == 0)
    odd_count = sum(1 for digit in str(ticket) if int(digit) % 2 == 1)

    if even_count == odd_count:
        print(ticket)
