import requests

# Функция для записи результатов в файл
def write_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as f:  # 'a' для добавления в конец файла
        f.write(content + "\n")


report_filename = "api_test_report.txt"

# Получение списка товаров
response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
result = f"Получение списка товаров: {response.status_code}, {response.json()}"
print(result)
write_to_file(report_filename, result)

# Получение информации о конкретном товаре
response = requests.get("https://petstore.swagger.io/v2/pet/1")
result = f"Получение информации о товаре с ID 1: {response.status_code}, {response.json()}"
print(result)
write_to_file(report_filename, result)

# Добавление нового товара
new_product = {
    "id": 0,
    "name": "Корм для собак",
    "category": {"id": 1, "name": "Корм"},
    "photoUrls": [],
    "tags": [],
    "status": "available"
}
response = requests.post("https://petstore.swagger.io/v2/pet", json=new_product)
result = f"Добавление нового товара: {response.status_code}, {response.json()}"
print(result)
write_to_file(report_filename, result)

# Обновление информации о товаре
updated_product = {
    "id": 1,  # Замените на актуальный ID, если необходимо
    "name": "Обновленный корм для собак",
    "category": {"id": 1, "name": "Корм"},
    "photoUrls": [],
    "tags": [],
    "status": "available"
}
response = requests.put("https://petstore.swagger.io/v2/pet", json=updated_product)
result = f"Обновление информации о товаре: {response.status_code}, {response.json()}"
print(result)
write_to_file(report_filename, result)

# Удаление товара
response = requests.delete("https://petstore.swagger.io/v2/pet/1")
result = f"Удаление товара с ID 1: {response.status_code}"
print(result)
write_to_file(report_filename, result)

print(f"Результаты тестирования сохранены в файл: {report_filename}")