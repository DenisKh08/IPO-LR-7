#Хитрик Денис
#2

import json

FILE_NAME = "task_2/dump.json"

def find_qualification(data, qual_id):
    for item in data:
        if item.get("model") == "data.skill" and item.get("pk") == qual_id: 
            print("=" * 10 + " Найдено " + "=" * 10)
            current_code = item['fields']['code']
            current_title = item['fields']['title']
            print(f"{current_code} >> {current_title}")
            return item
    return None

def main():
    try:
        with open(FILE_NAME, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{FILE_NAME}' не найден.") 
        return
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON из файла '{FILE_NAME}'.") 
        return

    user_input = int(input("Введите номер квалификации (pk): "))

    found_qual = find_qualification(data, user_input)

    if found_qual:
        print()
    else:
        print("=" * 10 + " Не найдено " + "=" * 10)

if __name__ == "__main__":
    main()