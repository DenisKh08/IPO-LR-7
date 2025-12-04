#Хитрик Денис
#2

print("start_code")
print(" ")

books = [
    {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    {"title": "Дом в котором", "author": "Мариам Петросян", "year": 2009},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
    {"title": "Три товарища", "author": "Эрих Мария Ремарк", "year": 1936}
]

for i, book in enumerate(books, start=1):
    print('-' * 25, f"Книга {i}", '-' * 25)
    print(f"Название: {book['title']}, Автор: {book['author']}")
    print('-' * 25, f"{book['year']}", '-' * 25)
    print(" ")

print("end_code")