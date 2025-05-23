
# Выполнил: Машук Ю.Н.
# Группа: МС-32



# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте пример данных ниже, при необходимости измените его для
# проверки правильности решения

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]


def vacant_compartments(data):
    """Вернуть список полностью свободных купе. Нумерация купе идет с 1."""
    return [i + 1 for i, compartment in enumerate(data) if all(seat is None for seat in compartment.values())]


def vacant_seats(data, compartments_condition=None, seat_condition=None):
    """Вернуть список свободных мест с учетом условий."""
    result = []
    for i, compartment in enumerate(data):
        if compartments_condition and not compartments_condition(compartment):
            continue
        for seat_num, occupant in compartment.items():
            if seat_condition and not seat_condition(seat_num, occupant):
                continue
            if occupant is None:
                result.append((i + 1, seat_num))
    return result


def is_same_sex_and_vacant(compartment, sex):
    """Проверяет, есть ли свободные места, а остальные пассажиры одного пола."""
    occupied = [s for s in compartment.values() if s is not None]
    return all(passenger == sex for passenger in occupied) and any(s is None for s in compartment.values())


print("Полностью свободные купе:", vacant_compartments(data))
print("Свободные места:", vacant_seats(data))
print("Свободные нижние места:", vacant_seats(data, seat_condition=lambda seat, value: seat % 2 != 0))
print("Свободные верхние места:", vacant_seats(data, seat_condition=lambda seat, value: seat % 2 == 0))
print("Свободные места в купе с мужской компанией:", vacant_seats(data, compartments_condition=lambda x: is_same_sex_and_vacant(x, "м")))
print("Свободные места в купе с женской компанией:", vacant_seats(data, compartments_condition=lambda x: is_same_sex_and_vacant(x, "ж")))



# --------------
# Пример вывода:
#
# [5, 7]
# [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3),
#  (7, 4), (8, 3), (9, 2), (9, 3)]
# [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# [(8, 3)]
# [(9, 2), (9, 3)]
