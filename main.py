# Исходные данные для формирования словаря
# Импортирование необходимых модулей
import json
import re
from random import randint, triangular
from conf import MODEL

print(MODEL)
from faker import Faker


# Функция для передачи заголовка книги
def task_title():
    with open('books.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")


# Функция для генерации случайных имен для авторов книги
def task_autor():
    author_name = Faker()
    print(author_name.name())
    for _ in range(2):
        author = (author_name.name())
        pass


# Функция для генерации ISBN для книги
def task_isbn():
    isbn = Faker()
    Faker.seed(0)
    for _ in range(1):
        pass


# Функция для генерации года для книги
def task_year():
    year = randint(1954, 2021)
    print(year)
    pass


# Функция для генерации общего количества страниц книги
def task_pages():
    pages = randint(200, 878)
    pass


# Функция для цены книги в рублях
def task_price():
    price = randint(200, 1500)
    pass

# Функция для генарации рейтинга книги
def task_price():
    rating = triangular(1, 10)
    print(rating)
    pass

# fields = {}
# Словарь
# if __name__ == "__main__":

# def task_for_book():


# with open("books.txt", "r") as f:
