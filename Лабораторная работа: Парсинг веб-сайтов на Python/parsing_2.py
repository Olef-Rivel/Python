import requests
import csv
from bs4 import BeautifulSoup
import os


#  Запрос HTML-страницы
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Проверка успешного запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')  # Парсим HTML

    news_items = soup.find_all('tr', class_='athing submission')

    with open('news_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link', 'Comments'])

        for item in news_items:
            title = item.find('span', class_='titleline').find('a').text
            link = item.find('span', class_='titleline').find('a')['href']
            # Находим следующий tr для получения комментариев
            next_tr = item.find_next_sibling('tr')
            comments = next_tr.find('span', class_='subline').find_all('a')[-1].text
            writer.writerow([title, link, comments])

print("Данные сохранены в news_data.csv")
os.startfile("news_data.csv")