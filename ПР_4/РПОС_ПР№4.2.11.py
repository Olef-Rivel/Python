
# Выполнил: Машук Ю.Н.
# Группа: МС-32


def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): свдиг.

    Результат:
        str: измененная строка."""
    # Набор кириллических букв
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    result = ""
    for char in text:
        if char.lower() in letters:  # Проверяем, является ли символ буквой
            is_upper = char.isupper()  # Проверяем, является ли буква заглавной
            idx = letters.index(char.lower())  # Получаем индекс буквы
            new_idx = (idx + shift) % len(letters)  # Смещаем индекс
            new_char = letters[new_idx]  # Получаем новый символ
            result += new_char.upper() if is_upper else new_char  # Учитываем регистр
        else:
            result += char  # Знаки препинания и пробелы остаются неизменными
    return result


text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))

# Шифрование
encoded = ceasar(text, shift)

# Дешифрование
decoded = ceasar(encoded, -shift)

print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++

