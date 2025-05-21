def caesar_cipher(text, shift, language="eng", mode="encrypt"):
    if language == "eng":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif language == "rus":
        alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
                   "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    else:
        return "Ошибка: неизвестный язык"

    shift = shift if mode == "encrypt" else -shift
    result = ""

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char  # Оставляем знаки препинания и пробелы

    return result

# --- Ввод данных ---
text = input("Введите текст: ")
language = input("Выберите язык (eng/rus): ").strip().lower()
mode = input("Выберите режим (encrypt/decrypt): ").strip().lower()
shift = int(input("Введите шаг сдвига: "))

# --- Запуск шифрования или дешифрования ---
output = caesar_cipher(text, shift, language, mode)
print("\nРезультат:", output)
