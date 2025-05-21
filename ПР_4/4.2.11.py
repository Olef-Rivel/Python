def caesar_cipher(text, shift, decrypt=False):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    shift = -shift if decrypt else shift  # Если нужно расшифровать, меняем знак смещения
    result = ''

    for char in text:
        if char.lower() in alphabet:  # Проверяем, является ли символ буквой русского алфавита
            is_upper = char.isupper()  # Сохраняем регистр
            new_index = (alphabet.index(char.lower()) + shift) % len(alphabet)
            new_char = alphabet[new_index]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char  # Знаки препинания и пробелы не изменяются

    return result

sentence = input("Введите текст для шифрования: ")
shift_value = int(input("Введите сдвиг: "))

encrypted_text = caesar_cipher(sentence, shift_value)
print(f"Зашифрованный текст: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, shift_value, decrypt=True)
print(f"Расшифрованный текст: {decrypted_text}")
