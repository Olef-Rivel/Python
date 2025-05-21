from collections import Counter

def calculate_election_results(votes):
    # Исключаем испорченные бланки (-1)
    valid_votes = [vote for vote in votes if vote > 0]

    # Подсчитываем количество голосов за каждую партию
    vote_counts = Counter(valid_votes)

    # Общее количество голосов
    total_votes = sum(vote_counts.values())

    # Формируем список результатов с процентами
    results = sorted([(party, count, round(count / total_votes * 100, 2)) for party, count in vote_counts.items()], 
                     key=lambda x: x[1], reverse=True)

    # Выводим результаты
    for i, (party, count, percentage) in enumerate(results, start=1):
        print(f"{i}. Партия №{party} | {count} | {percentage}%")

# Пример списка голосов
votes = [1, 3, 2, 2, 2, 5, -1, 4, 4, 2, 3, 5, 2, 1, -1, 4, 2, 2, 3, 5, 4, 2, 1, 2, 2, 4, -1]

calculate_election_results(votes)
