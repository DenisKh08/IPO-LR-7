#Хитрик Денис
#2

import json
import os

print("start code")
print("")

# функции для работа с файлами
def initialize_file():
#Инициализация файла с начальными данными
    filename = "flowers.json"
    
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

    return filename


def load_data(filename):
    """Загрузка данных из файла"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(filename, data):
    """Сохранение данных в файл"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


# ФУНКЦИИ ВАЛИДАЦИИ 
def validate_int_input(prompt, min_value=None, max_value=None):
    """Валидация целочисленного ввода"""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Пустой ввод")
            
            value_int = int(value)
            
            if min_value is not None and value_int < min_value:
                print(f"Ошибка: число должно быть не меньше {min_value}")
                continue
                
            if max_value is not None and value_int > max_value:
                print(f"Ошибка: число должно быть не больше {max_value}")
                continue
                
            return value_int
        except ValueError as e:
            if "Пустой ввод" in str(e):
                print("Ошибка: поле не может быть пустым")
            else:
                print("Ошибка: введите целое число")


def validate_float_input(prompt, min_value=0.0):
    """Валидация ввода числа с плавающей точкой"""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Пустой ввод")
            
            value_float = float(value)
            
            if min_value is not None and value_float < min_value:
                print(f"Ошибка: число должно быть не меньше {min_value}")
                continue
                
            return value_float
        except ValueError as e:
            if "Пустой ввод" in str(e):
                print("Ошибка: поле не может быть пустым")
            else:
                print("Ошибка: введите число")


def validate_string_input(prompt, min_length=1):
    """Валидация строкового ввода"""
    while True:
        value = input(prompt).strip()
        
        if len(value) < min_length:
            print(f"Ошибка: введите не менее {min_length} символов")
            continue
            
        return value


def validate_bool_input(prompt):
    """Валидация булевого ввода"""
    while True:
        value = input(prompt).strip().lower()
        
        if value in ["да", "yes", "1", "true", "д", "y"]:
            return True
        elif value in ["нет", "no", "0", "false", "н", "n"]:
            return False
        else:
            print("Ошибка: введите 'да' или 'нет'")

#ФУНКЦИИ ОТОБРАЖЕНИЯ ДАННЫХ
def display_menu():
    """Отображение главного меню"""
    print("\n" + "="*50)
    print("МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ ЦВЕТОВ")
    print("="*50)
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")
    print("="*50)

#выводит всю инф о цветах(1 пункт меню)
def display_all_flowers(flowers):
    """Отображение всех записей"""
    if not flowers:
        print("\nБаза данных пуста!")
        return

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

#Отображение записи по ID(2 пункт)
def display_flower_by_id(flowers):
    search_id = validate_int_input("Введите ID для поиска: ")
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


#добавляет запись(3 пункт)
def add_flower(filename, flowers):
    print("\nДобавление новой записи:")
    
# Находим максимальный ID
    max_id = max([flower["id"] for flower in flowers]) if flowers else 0
    new_id = max_id + 1
    
# Запрашиваем данные с валидацией
    name = validate_string_input("Введите название цветка: ", min_length=2)
    latin_name = validate_string_input("Введите латинское название: ", min_length=2)
    is_red_book = validate_bool_input("Цветок краснокнижный? (да/нет): ")
    price = validate_float_input("Введите цену цветка: ", min_value=0.0)
    
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
    save_data(filename, flowers)
    
    print(f"Запись с ID {new_id} успешно добавлена!")
    
    return flowers

#Удаление записи по ID
def delete_flower(filename, flowers):
    delete_id = validate_int_input("Введите ID для удаления: ")
    
# Ищем запись для удаления
    found_index = -1
    for i, flower in enumerate(flowers):
        if flower["id"] == delete_id:
            found_index = i
            break
    
    if found_index != -1:
# Подтверждение удаления
        flower_to_delete = flowers[found_index]
        confirm = validate_bool_input(f"Вы уверены, что хотите удалить запись '{flower_to_delete['name']}' (ID: {delete_id})? (да/нет): ")

        if confirm:
# Удаляем запись
            deleted_flower = flowers.pop(found_index)

# Сохраняем обновленные данные
            save_data(filename, flowers)


            print(f"Запись с ID {delete_id} ('{deleted_flower['name']}') успешно удалена!")
        else:
            print("Удаление отменено.")
    else:
        print(f"Запись с ID {delete_id} не найдена!")

    return flowers


#ГЛАВНАЯ ФУНКЦИЯ
def main():
    print("start code")
    print(" ")

# Инициализация файла
    filename = initialize_file()
    
# Счетчик операций
    operations_count = 0
    
# Основной цикл программы
    while True:
        display_menu()
        
        choice = validate_int_input("Выберите пункт меню (1-5): ", min_value=1, max_value=5)
        
        if choice == 1:
# Вывести все записи
            operations_count += 1
            flowers = load_data(filename)
            display_all_flowers(flowers)
            
        elif choice == 2:
# Вывести запись по ID
            operations_count += 1
            flowers = load_data(filename)
            display_flower_by_id(flowers)
            
        elif choice == 3:
# Добавить запись
            operations_count += 1
            flowers = load_data(filename)
            flowers = add_flower(filename, flowers)
            
        elif choice == 4:
# Удалить запись по ID
            operations_count += 1
            flowers = load_data(filename)
            flowers = delete_flower(filename, flowers)
            
        elif choice == 5:
# Выйти из программы
            print(f"\nКоличество выполненных операций: {operations_count}")
            print("Выход из программы. До свидания!")
            break
    
    print(" ")
    print("end code")

if __name__ == "__main__":
    main()