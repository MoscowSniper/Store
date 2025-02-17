import requests
import json
from datetime import datetime


# JSON REPORT FUNCTION
def write_report(report_data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"api_test_report_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report_data)

    print(f"REPORT SAVED TO: {filename}")


def test_petstore_api():
    report_lines = []

    # GET
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    report_lines.append(f"Получение списка товаров: {response.status_code}")

    pet_id = 1
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
    if response.status_code == 200:
        report_lines.append(f"Получение информации о товаре с ID {pet_id}: {response.status_code}")
    else:
        report_lines.append(
            f"Получение информации о товаре с ID {pet_id}: {response.status_code} - {response.json()['message']}")

    # POST
    new_product = {
        "id": 0,
        "name": "Корм для собак",
        "category": {"id": 1, "name": "Корм"},
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=new_product)
    report_lines.append(f"Добавление нового товара: {response.status_code} - {response.json()}")

    # PUT
    if response.status_code == 200 or response.status_code == 201:
        updated_product = {
            "id": response.json()['id'],
            "name": "Обновленный корм для собак",
            "category": {"id": 1, "name": "Корм"},
            "photoUrls": [],
            "tags": [],
            "status": "available"
        }
        response = requests.put("https://petstore.swagger.io/v2/pet", json=updated_product)
        report_lines.append(f"Обновление информации о товаре: {response.status_code} - {response.json()}")

    # DELETE
    if response.status_code == 200:
        response = requests.delete(f"https://petstore.swagger.io/v2/pet/{updated_product['id']}")
        report_lines.append(f"Удаление товара с ID {updated_product['id']}: {response.status_code}")

    # PRINTING REPORT DATA
    report_data = "\n".join(report_lines)
    write_report(report_data)


# RUN
test_petstore_api()