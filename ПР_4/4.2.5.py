from datetime import datetime, timedelta

def another_date(day, month, year, delta=1):
    def calculate_date(day, month, year, offset):
        date = datetime(year, month, day) + timedelta(days=offset)
        return date.strftime("%d.%m.%Y")
    
    return calculate_date(day, month, year, delta)

# Ввод даты пользователем
day, month, year = map(int, input("Введите дату (дд.мм.гггг): ").split('.'))

# Вывод результатов
print("Вчерашняя дата:", another_date(day, month, year, -1))
print("Завтрашняя дата:", another_date(day, month, year, 1))
