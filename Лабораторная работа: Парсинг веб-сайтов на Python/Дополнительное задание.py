from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# URL главной страницы
base_url = "https://www.onliner.by/"

# Запускаем WebDriver
driver = webdriver.Chrome()
driver.get(base_url)

# Ожидание загрузки списка разделов с товарами
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.project-navigation__list.project-navigation__list_secondary')))

# Находим все разделы с товарами
lists = driver.find_elements(By.CSS_SELECTOR, '.project-navigation__list.project-navigation__list_secondary')

# Извлекаем ссылки на разделы
category_links = [link.get_attribute('href') for list_elem in lists for link in list_elem.find_elements(By.TAG_NAME, 'a')]

print(" Найденные ссылки на разделы:", category_links)



products = [] #список товаров
# Обходим каждый раздел с товарами
for category in category_links:
    driver.get(category)  # Переход на страницу раздела
    
    try:
        # Ожидание загрузки списка товаров
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.catalog-form__offers-part')))

        # Находим товары
        product_name = driver.find_elements(By.CSS_SELECTOR, 'a.catalog-form__link_primary-additional')
        product_rating = driver.find_elements(By.CSS_SELECTOR, 'a.catalog-form__rating span.catalog-form__rating-value')

        # Формируем списки
        product_names = [name.text for name in product_name]
        products_rating = [rating.text for rating in product_rating]

        # зазделяем список с именами (там еёщ цена)
        prod_name = product_names[1::2] # Чётные индексы (названия)
        prod_price = product_names[0::2] # Нечётные индексы (цены)



        for name, price, rating in zip(prod_name, prod_price, products_rating):
            products.append({
            "Товар" : name,
            "Цена" : price,
            "Рейтинг" : rating,
        })
            

    except Exception as e:
        print(f" Ошибка при обработке раздела: {category}. Детали: {e}")

# Вывод итогового списка товаров
print("\n Найденные товары:")
for product in products:
    print(product)
    print(f"Кличество товаров: {len(products)}")


with open('products_onliner.json', 'w', encoding='utf-8') as f: #записать
    json.dump(products, f, ensure_ascii=False, indent=4)

# Завершаем работу браузера
driver.quit()
