# Выполнил: Машук Ю.Н.
# Группа: МС-32

def is_leap(year):
    if year % 4 != 0:
        return False

    if year % 100 != 0:
        return True

    if year % 400 == 0:
        return True
    else:
        return False


def days(month, year):
    list_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]

    if is_leap(year) and month == 2:
        return list_months[13-1]
    
    return list_months[month-1]


def another_date(day, month, year, delta=1):
    
    def previous_date(day, month, year):
    
        if day >= 2:
            day -= 1
        
        elif month >= 2:
            month -= 1
            day = days(month, year)
        
        else:
            year -= 1
            month = 12
            day = days(month, year)

        return day, month, year


    def next_date(day, month, year):

        if day < days(month, year):
            day += 1
        
        elif month < 12:
            month += 1
            day = 1
        
        else:
            year += 1
            month = 1
            day = 1

        return day, month, year


    if delta == 0:
        return day, month, year
    
    elif delta > 0:
        for i in range(delta):
            day, month, year = next_date(day, month, year)

    else:
        for i in range(abs(delta)):
            day, month, year = previous_date(day, month, year)

    return day, month, year
        




values = list()
values = input("День, месяц, год через пробел: ").split()
delta = int(input("Свдиг (может быть отрицательным): "))
day = int(values[0])
month = int(values[1])
year = int(values[2])



day, month, year = another_date(day, month, year, delta)

print(f"Новый день: {str(day).zfill(2)}/{str(month).zfill(2)}/{year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): -2
# Новый день: 30/12/1999
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): 2
# Новый день: 03/01/2000
