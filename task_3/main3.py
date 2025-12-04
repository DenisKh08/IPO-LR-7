#Хитрик Денис
#2

import json
import os

print("start code")
print(" ")
# Название файла для хранения данных
filename = "flowers.json"

# Счетчик операций
operations_count = 0

# Если файл не существует, создаем его с 5 начальными записями
if not os.path.exists(filename):
    initial_data = [
        {
            "id": 1,
            "name": "Роза",
            "latin_name": "Rosa",
            "is_red_book_flower": False,
            "price": 150.0
        },
        {
            "id": 2,
            "name": "Тюльпан",
            "latin_name": "Tulipa",
            "is_red_book_flower": False,
            "price": 80.0
        },
        {
            "id": 3,
            "name": "Подснежник",
            "latin_name": "Galanthus",
            "is_red_book_flower": True,
            "price": 200.0
        },
        {
            "id": 4,
            "name": "Орхидея",
            "latin_name": "Orchidaceae",
            "is_red_book_flower": False,
            "price": 300.0
        },
        {
            "id": 5,
            "name": "Кувшинка",
            "latin_name": "Nymphaea",
            "is_red_book_flower": True,
            "price": 250.0
        }
    ]
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=2)
    print("Создан файл с 5 начальными записями.")

# Основной цикл программы
while True:
    print("\n" + "="*50)
    print("МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ ЦВЕТОВ")
    print("="*50)
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")
    print("="*50)
    
    choice = input("Выберите пункт меню (1-5): ").strip()
    
    if choice == "1":
        # Вывести все записи
        operations_count += 1
        with open(filename, "r", encoding="utf-8") as file:
            flowers = json.load(file)
        
        if not flowers:
            print("\nБаза данных пуста!")
        else:
            print(f"\nВсего записей: {len(flowers)}")
            print("-" * 70)
            for i, flower in enumerate(flowers, 1):
                red_book = "Да" if flower["is_red_book_flower"] else "Нет"
                print(f"Запись #{i}")
                print(f"  ID: {flower['id']}")
                print(f"  Название: {flower['name']}")
                print(f"  Латинское название: {flower['latin_name']}")
                print(f"  Краснокнижный: {red_book}")
                print(f"  Цена: {flower['price']} руб.")
                print("-" * 70)
    
    elif choice == "2":
        # Вывести запись по ID
        operations_count += 1
        try:
            search_id = int(input("Введите ID для поиска: ").strip())
        except ValueError:
            print("Ошибка: ID должен быть числом!")
            continue
        
        with open(filename, "r", encoding="utf-8") as file:
            flowers = json.load(file)
        
        found = False
        for i, flower in enumerate(flowers):
            if flower["id"] == search_id:
                found = True
                red_book = "Да" if flower["is_red_book_flower"] else "Нет"
                print(f"\nНайдена запись (позиция в списке: {i+1}):")
                print(f"  ID: {flower['id']}")
                print(f"  Название: {flower['name']}")
                print(f"  Латинское название: {flower['latin_name']}")
                print(f"  Краснокнижный: {red_book}")
                print(f"  Цена: {flower['price']} руб.")
                break
        
        if not found:
            print(f"Запись с ID {search_id} не найдена!")
    
    elif choice == "3":
        # Добавить запись
        operations_count += 1
        
        # Читаем существующие данные
        with open(filename, "r", encoding="utf-8") as file:
            flowers = json.load(file)
        
        # Находим максимальный ID
        max_id = max([flower["id"] for flower in flowers]) if flowers else 0
        
        print("\nДобавление новой записи:")
        
        # Запрашиваем данные
        new_id = max_id + 1
        name = input("Введите название цветка: ").strip()
        latin_name = input("Введите латинское название: ").strip()
        
        red_book_input = input("Цветок краснокнижный? (да/нет): ").strip().lower()
        is_red_book = red_book_input in ["да", "yes", "1", "true"]
        
        try:
            price = float(input("Введите цену цветка: ").strip())
        except ValueError:
            print("Ошибка: цена должна быть числом!")
            continue
        
        # Создаем новую запись
        new_flower = {
            "id": new_id,
            "name": name,
            "latin_name": latin_name,
            "is_red_book_flower": is_red_book,
            "price": price
        }
        
        # Добавляем запись
        flowers.append(new_flower)
        
        # Сохраняем в файл
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(flowers, file, ensure_ascii=False, indent=2)
        
        print(f"Запись с ID {new_id} успешно добавлена!")
    
    elif choice == "4":
        # Удалить запись по ID
        operations_count += 1
        
        try:
            delete_id = int(input("Введите ID для удаления: ").strip())
        except ValueError:
            print("Ошибка: ID должен быть числом!")
            continue
        
        # Читаем данные
        with open(filename, "r", encoding="utf-8") as file:
            flowers = json.load(file)
        
        # Ищем запись для удаления
        found_index = -1
        for i, flower in enumerate(flowers):
            if flower["id"] == delete_id:
                found_index = i
                break
        
        if found_index != -1:
            # Удаляем запись
            deleted_flower = flowers.pop(found_index)
            
            # Сохраняем обновленные данные
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(flowers, file, ensure_ascii=False, indent=2)
            
            print(f"Запись с ID {delete_id} ('{deleted_flower['name']}') успешно удалена!")
        else:
            print(f"Запись с ID {delete_id} не найдена!")
    
    elif choice == "5":
        # Выйти из программы
        print(f"\nКоличество выполненных операций: {operations_count}")
        print("Выход из программы. До свидания!")
        break
    
    else:
        print("Неверный выбор! Пожалуйста, выберите пункт от 1 до 5.")

print(" ")
print("end code")