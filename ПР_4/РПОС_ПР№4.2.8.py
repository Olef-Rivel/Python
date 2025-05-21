# Выполнил: Машук Ю.Н.
# Группа: МС-32

def print_with_border(string, char):
    """Рисует рамку из символа 'char' вокруг строки 'string'.

    Параметры:
        string (str): строка, которую нужно обрамить.
        char (str): символ, используемый для рамки.

    Результат:
        None: выводит строку с рамкой в консоль.
    """
    border = char * (len(string) + 2)  # Верхняя и нижняя граница
    print(border)
    print(f"{char}{string}{char}")
    print(border)

# Ввод данных
s = input("Введите строку: ")
k = input("Введите символ: ")

# Вывод результата
print_with_border(s, k)
