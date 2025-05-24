from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import time  # Импортируем модуль для пауз
import json

# URL главной страницы
base_url = "https://shop.mts.by/tv/tv2/"
products = []

# Загружаем HTML и ищем навигационный блок
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')
nav = soup.find("nav", class_='nav nav--header')

# Получаем ссылки на страницы пагинации
page_links = [urljoin(base_url, a["href"]) for a in nav.find_all("a", href=True)] if nav else [base_url]

# Парсим каждую страницу
for url in page_links:
    

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим блоки товаров
        items = soup.find_all("div", class_="card-product__info")

        for item in items:
            # Извлекаем название
            title_elem = item.find("h3", class_="card-product__title")
            title = title_elem.text.strip() if title_elem else "Нет названия"

            # Извлекаем все цены
            price_elems = item.find("div", class_="card-product__prices").find_all("p", class_="card-product__price") if item.find("div", class_="card-product__prices") else []
            prices = [price_elem.find("span", class_="num").text.strip() for price_elem in price_elems if price_elem.find("span", class_="num")]
            price = ", ".join(prices) if prices else "Нет цены"

            # Извлекаем характеристики товара
            characteristics = item.find("div", class_="card-product__chars")
            char_list = [char.text.strip() for char in characteristics.find_all("p", class_="card-product__char")] if characteristics else []
            char_text = "; ".join(char_list) if char_list else "Нет характеристик"

            products.append({
                "Название": title,
                "Цена(ы)": price,
                "Характеристики": char_text
            })
        
        print(f"✅ Успешно обработана страница: {url}")
    else:
        print(f"⚠ Ошибка загрузки {url}: {response.status_code}")

    print(f" Ожидание 2 секунды перед запросом к {url}...")
    time.sleep(2)  # Задержка перед запросом

with open('products.json', 'w', encoding='utf-8') as f: #записать
    json.dump(products, f, ensure_ascii=False, indent=4)

with open('products.json', 'r', encoding='utf-8') as f: #читать
    data = json.load(f)  
    print(data)  

# Вывод итогового списка товаров
print("\n🔍 Найденные товары:")
for product in products:
    print(product)

print(f"Собрано {len(products)} товара")
