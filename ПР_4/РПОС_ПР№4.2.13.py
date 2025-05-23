
# Выполнил: Машук Ю.Н.
# Группа: МС-32



# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте значения 'votes', при необходимости измените его для
# проверки правильности решения

votes = [
    2, 3, -1, 2, 5, 1, 1, 4, 1, 1, 1, 3, 1, 3, 5, -1, 5, 2, 5, 5,
    3, 3, 2, 3, 3, 2, 2, 1, 3, 2, 5, 2, 2, 4, 1, 1, 3, 2, 2, 3, 3,
    3, 1, 4, 2, 1, 4, 2, 3, 3, 3, -1, 5, 3, 1, 4, 5, 1, 1, 3, 3,
    3, -1, 5, 3, 3, 2, 5, 1, 1, 5, -1, 1, 2, 2, 3, -1, 4, 2, 5, 4,
    2, -1, 3, 1, 4, 3, 5, 4, 1, 5, 3, 2, 4, 2, 1, 3, 4, 1, 1, 3, 4
]

parties = {
    1: "Партия №1", 2: "Партия №2", 3: "Партия №3",
    4: "Партия №4", 5: "Партия №5", -1: "Испорчено"
}


def parties_votes(parties, votes):
    votes_count = {name: 0 for name in parties.values()}  # Инициализация подсчета голосов

    for vote in votes:
        votes_count[parties[vote]] += 1

    return votes_count


def print_results(votes_for_p):

    total_votes = sum(votes_for_p.values())  # Общее количество голосов
    sorted_results = sorted(votes_for_p.items(), key=lambda x: x[1], reverse=True)  # Сортировка по количеству голосов

    for i, (party, count) in enumerate(sorted_results, start=1):
        percentage = (count / total_votes) * 100  # Вычисление процента голосов
        print(f"{i}. {party} | {count} | {percentage:.2f}%")


print_results(parties_votes(parties, votes))

# --------------
# Пример вывода:
#
# 1. Партия №3 | 27 | 26.47%
# 2. Партия №1 | 22 | 21.57%
# 3. Партия №2 | 20 | 19.61%
# 4. Партия №5 | 14 | 13.73%
# 5. Партия №4 | 12 | 11.76%
# 6. Испорчено |  7 |  6.86%
