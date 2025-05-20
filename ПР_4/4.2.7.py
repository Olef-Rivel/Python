# Ввод предложений
n = int(input("Введите количество предложений: "))
sentences = [input(f"Введите предложение {i+1}: ") for i in range(n)]

# Подсчет предложений с цифрами
count = sum(1 for sentence in sentences if any(char.isdigit() for char in sentence))

print(f"Количество предложений с цифрами: {count}")
