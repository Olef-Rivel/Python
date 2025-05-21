def count_characters(text):
    text = text.lower()  # Игнорируем регистр
    char_count = {}

    for char in text:
        if char.isalpha():  # Учитываем только буквы
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    for char, count in char_count.items():
        print(f"{char} = {count}")

sentence = input("Введите предложение: ")
count_characters(sentence)
