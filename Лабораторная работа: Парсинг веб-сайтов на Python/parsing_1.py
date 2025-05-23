import requests
from bs4 import BeautifulSoup

#  Запрос HTML-страницы
url = "https://www.apple.com/"
response = requests.get(url)

# Проверка успешного запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')  # Парсим HTML

    # Выводим заголовки
    # print(soup.head)  # Заголовок <head>
    # print(soup.body)  # Первый заголовок <body>

    headers = soup.find_all(['h1', 'h2', 'h3', 'h4' , 'h5', 'h6'])
    links = soup.find_all('a')
    # print(headers)

    
    # Убираем дубликаты с помощью `set()`
    # unique_headers = set(header.get_text(strip=True) for header in headers)

    #Вывод всех заголовков без повторяющихся 
    for header in headers:
        # print(f'Заголовок на странице ' + header.text.strip())
        text = header.get_text(separator=" ", strip=True)  # Убираем пробелы и переносы строк
        print(f'Заголовок на странице {text}')

    
    for link in links:
        href = link.get("href")  # Получаем URL ссылки
        text_links = link.get_text(separator=" ", strip=True)  # Текст внутри ссылки
        print(f'Ссылка {href} |  Описание {text_links}')


else:
    print(f"Ошибка! Код {response.status_code}")
