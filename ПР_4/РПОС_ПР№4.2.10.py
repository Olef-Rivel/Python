
# Выполнил: Машук Ю.Н.
# Группа: МС-32



def sentence_stats(sentence):
    """Вернуть символьную статистику 'sentence'. Регистр не учитывается."""
    
    sentence_stats_dict = {}  # Переименуем, чтобы избежать путаницы

    sentence = sentence.lower()  # Приводим текст к нижнему регистру
    
    for char in sentence:
        if char in sentence_stats_dict:
            sentence_stats_dict[char] += 1
        else:
            sentence_stats_dict[char] = 1

    return sentence_stats_dict  # Возвращаем результат вместо print


s = input("Введите предложение: ")
print(sentence_stats(s))  # Передаём введённое пользователем предложение


# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}
