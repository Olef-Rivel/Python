# Выполнил: Машук Ю.Н.
# Группа: МС-32

def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        year (int): год.

    Результат:
        bool: True - если год високосный, False - если нет.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        month (int): номер месяца (1-12).
        year (int): год.

    Результат:
        int: количество дней в месяце.
    """
    days_in_month = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]

def previous_date(day, month, year):
    """Вернуть день, месяц, год предыдущего дня.

    Параметры:
        day (int): день.
        month (int): месяц.
        year (int): год.

    Результат:
        tuple: (день, месяц, год) предыдущего дня.
    """
    if day > 1:
        return day - 1, month, year
    elif month > 1:
        return days(month - 1, year), month - 1, year
    else:
        return 31, 12, year - 1

def next_date(day, month, year):
    """Вернуть день, месяц, год следующего дня.

    Параметры:
        day (int): день.
        month (int): месяц.
        year (int): год.

    Результат:
        tuple: (день, месяц, год) следующего дня.
    """
    if day < days(month, year):
        return day + 1, month, year
    elif month < 12:
        return 1, month + 1, year
    else:
        return 1, 1, year + 1

# Ввод данных
day, month, year = map(int, input("День, месяц, год через пробел: ").split())

# Вывод результатов
prev_day, prev_month, prev_year = previous_date(day, month, year)
next_day, next_month, next_year = next_date(day, month, year)

print(f"Предыдущий день: {prev_day:02}/{prev_month:02}/{prev_year}")
print(f"Следующий день: {next_day:02}/{next_month:02}/{next_year}")
