# Функция для определения полностью свободных купе
def get_free_compartments(train):
    # Перебираем купе и проверяем, заняты ли все места
    free_compartments = [index + 1 for index, coupe in enumerate(train) if all(place is None for place in coupe.values())]
    return free_compartments

# Функция для нахождения всех свободных мест в вагоне
def get_free_seats(train):
    # Перебираем купе и места, проверяя, какие не заняты
    free_seats = [(index + 1, seat) for index, coupe in enumerate(train) for seat, occupant in coupe.items() if occupant is None]
    return free_seats

# Функция для нахождения свободных нижних или верхних мест
def get_free_seats_by_type(train, lower=True):
    # Если lower=True, ищем нижние места, иначе верхние
    free_seats = [(index + 1, seat) for index, coupe in enumerate(train) for seat, occupant in coupe.items()
                  if occupant is None and ((lower and seat % 2 != 0) or (not lower and seat % 2 == 0))]
    return free_seats

# Функция для нахождения свободных мест в купе с исключительно мужской компанией
def get_free_seats_male_only(train):
    free_seats = [(index + 1, seat) for index, coupe in enumerate(train) 
                  if any(occupant == 'м' for occupant in coupe.values())  # Проверяем, занято ли хотя бы одно место мужчиной
                  and all(occupant in {'м', None} for occupant in coupe.values())  # Проверяем, что все места либо свободны, либо заняты мужчинами
                  for seat, occupant in coupe.items() if occupant is None]
    return free_seats

# Функция для нахождения свободных мест в купе с исключительно женской компанией
def get_free_seats_female_only(train):
    free_seats = [(index + 1, seat) for index, coupe in enumerate(train) 
                  if any(occupant == 'ж' for occupant in coupe.values())  # Проверяем, занято ли хотя бы одно место женщиной
                  and all(occupant in {'ж', None} for occupant in coupe.values())  # Проверяем, что все места либо свободны, либо заняты женщинами
                  for seat, occupant in coupe.items() if occupant is None]
    return free_seats

# Пример данных — список купе с местами
train = [
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},  # Полностью свободное купе
    {1: 'м', 2: 'м', 3: None, 4: None},  # Купе с исключительно мужской компанией
    {1: 'ж', 2: 'ж', 3: 'ж', 4: None},  # Купе с исключительно женской компанией
]

# Выводим результаты работы функций
print("Полностью свободные купе:", get_free_compartments(train))
print("Свободные места в вагоне:", get_free_seats(train))
print("Свободные нижние места:", get_free_seats_by_type(train, lower=True))
print("Свободные верхние места:", get_free_seats_by_type(train, lower=False))
print("Свободные места в купе с исключительно мужской компанией:", get_free_seats_male_only(train))
print("Свободные места в купе с исключительно женской компанией:", get_free_seats_female_only(train))
