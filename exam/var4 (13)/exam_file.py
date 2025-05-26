import re
import json
from collections import Counter

# Функция для парсинга строки лога
def parse_log_line(line):
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?) (.*?) (.*?)" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return {
            "ip": match.group(1),
            "date_time": match.group(2),
            "method": match.group(3),
            "resource": match.group(4),
            "protocol": match.group(5),
            "status": match.group(6),
            "size": int(match.group(7))
        }
    return None

# Функция для записи в JSON
def save_to_json(report, filename="report.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Ошибка записи: {e}")

# Функция для анализа логов
def analyze_logs(file_path):
    ip_counter = Counter() #счётчик анализа данных
    resource_counter = Counter()
    method_counter = Counter()
    status_counter = Counter()
    data_volume_per_ip = Counter()
    data_volume_per_resource = Counter()
    total_size_successful = 0
    successful_requests = 0

    try:
        with open(file_path, 'r') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed: #если распознана обновляем сётчик
                    ip_counter[parsed["ip"]] += 1
                    resource_counter[parsed["resource"]] += 1
                    method_counter[parsed["method"]] += 1
                    status_counter[parsed["status"]] += 1

                    # Обработка переданных данных
                    data_volume_per_ip[parsed["ip"]] += parsed["size"] #Подсчет объема данных по IP
                    data_volume_per_resource[parsed["resource"]] += parsed["size"] #Подсчет объема данных по ресурсу

                    # Подсчет успешных запросов (код 200)
                    if parsed["status"] == "200":
                        total_size_successful += parsed["size"]
                        successful_requests += 1
                else:
                    print(f"Некорректная строка: {line.strip()}")
                   

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")
        return None

    # Рассчитываем средний размер успешного ответа
    avg_successful_size = total_size_successful / successful_requests if successful_requests else 0

    return {
        "requests_per_ip": dict(ip_counter),
        "top_5_resources": dict(resource_counter.most_common(5)),
        "requests_per_method": dict(method_counter),
        "requests_per_status": dict(status_counter),
        "total_data_transferred_success": total_size_successful,
        "top_5_resources_by_data": dict(data_volume_per_resource.most_common(5)),
        "avg_successful_response_size": avg_successful_size,
        "top_ip_by_data": max(data_volume_per_ip, key=data_volume_per_ip.get, default=None)
    }

# Основной код
if __name__ == "__main__":
    log_file = input("Введите путь к файлу логов: ")
    report = analyze_logs(log_file)

    if report:
        print("\n--- Log Analysis Report ---\n")
        print("Requests per IP:")
        for ip, count in report["requests_per_ip"].items():
            print(f"{ip}: {count}")

        print("\nTop 5 Requested URLs:")
        for url, count in report["top_5_resources"].items():
            print(f"{url}: {count}")

        print("\nRequests per HTTP Method:")
        for method, count in report["requests_per_method"].items():
            print(f"{method}: {count}")

        print("\nRequests per Status Code:")
        for status, count in report["requests_per_status"].items():
            print(f"{status}: {count}")

        print("\nTotal data transferred (successful requests - 200):", report["total_data_transferred_success"])

        print("\nTop 5 Resources by Data Volume:")
        for url, volume in report["top_5_resources_by_data"].items():
            print(f"{url}: {volume} bytes")

        print("\nAverage successful response size:", report["avg_successful_response_size"], "bytes")

        print("\nTop IP by Data Volume:", report["top_ip_by_data"])

        # Запись в JSON-файл
        filename = "report_file.json"
        save_to_json(report, filename)
