S = input("Введите строку: ")

if 0< len(S)< 100:
    print(" ".join(word.capitalize() for word in S.split()))
