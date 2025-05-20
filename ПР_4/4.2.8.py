def draw_frame(s, k):
    border = k * (len(s) + 4)  # Верхняя и нижняя границы
    print(border)
    print(f"{k} {s} {k}")  # Текст с боковыми рамками
    print(border)

# Ввод данных
s = input("Введите строку: ")
k = input("Введите символ рамки: ")

# Вызов функции
draw_frame(s, k)
