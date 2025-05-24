import requests
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import os

#  URL файла
file_url = "https://github.com/fixedsergey/datasets/raw/main/Cancer%20Deaths%20by%20Country%20and%20Type%20Dataset.zip"
zip_path = "cancer_data.zip"
extract_path = "cancer_data"

#  Проверка доступности файла
def check_file_availability(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:
            print(f"Файл доступен: {url}")
            return True
        else:
            print(f"Файл недоступен! Код ошибки: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при проверке файла: {e}")
        return False

#  Скачивание и разархивирование
def download_and_extract(url, zip_path, extract_path):
    response = requests.get(url, stream=True)
    with open(zip_path, "wb") as file:
        file.write(response.content)
    print("Файл загружен!")

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    print("Файл разархивирован!")

#  Чтение данных и построение графика
def plot_cancer_data(file_path):
    df = pd.read_csv(file_path)  # Укажи правильное имя файла

    #  Выведем названия всех столбцов
    print(df.columns)
    df.columns = df.columns.str.strip()  # Убираем пробелы в названиях столбцов


    country = input("Введите страну: ")
    cancer_type = input("Введите вид рака: ")

    filtered_df = df[df["Country"] == country]

    plt.figure(figsize=(10, 5))
    plt.plot(filtered_df["Year"], filtered_df[cancer_type], marker='o', linestyle='-', label=cancer_type)
    plt.xlabel("Год")
    plt.ylabel("Количество случаев")
    plt.title(f"Заболеваемость {cancer_type} в {country} по годам")
    plt.legend()
    plt.grid(True)
    plt.show()

#  Запуск
if check_file_availability(file_url):
    download_and_extract(file_url, zip_path, extract_path)
    csv_file = os.path.join(extract_path, "Cancer Deaths by Country and Type Dataset.csv")  # Укажи правильное имя файла
    plot_cancer_data(csv_file)
