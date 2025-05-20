from datetime import datetime, timedelta


# Функция для получения вчерашней даты
def yesterday(day, month, year):
    date = datetime(year, month, day) - timedelta(days=1)
    return date.strftime("%d.%m.%Y")  # Формат: DD.MM.YYYY

# Функция для получения завтрашней даты
def tomorrow(day, month, year):
    date = datetime(year, month, day) + timedelta(days=1)
    return date.strftime("%d.%m.%Y")  # Формат: DD.MM.YYYY

# Ввод даты пользователем
day, month, year = map(int, input("Введите дату (дд.мм.гггг): ").split('.'))

# Вывод результатов
print("Вчерашняя дата:", yesterday(day, month, year))
print("Завтрашняя дата:", tomorrow(day, month, year))
