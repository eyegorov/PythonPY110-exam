"""Исходные данные для формирования словаря"""
"""Импортирование необходимых модулей"""
import json
import re
from random import randint, triangular, choice
from conf import MODEL
print(MODEL)
from faker import Faker



#def pk(start=1):
    #"""Функция для инициализации начального значения счетчика"""
    #while True:
       # yield start
        #start += 1


def task_title():
    #"""Функция для вывода автора книги в случайном порядке из файла books.txt"""
    with open('books.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        random_lines = choice(text)
        return random_lines




def task_author():
    """Функция для генерации случайных имен авторов книги"""
    author_name = Faker()
    author_lst = []
    for _ in range(2):
        author_lst.append(author_name.name())
        return author_lst

def task_isbn():
    """Функция для генерации ISBN для книги"""
    random_isbn = Faker()
    for _ in range(1):                                                  #https://dvsemenov.ru/generaciya-sluchajnyh-dannyh-s-pomoshchyu-faker-v-python/
        isbn = random_isbn.numerify(text='%%%-%-%%%%-%%%%-%%%-%%')
        return isbn


def task_year():
    """Функция для генерации года для книги"""
    year = randint(1954, 2021)
    return year

def task_pages():
    """Функция для генерации общего количества страниц книги"""
    pages = randint(200, 878)
    return pages

def task_price():
    """Функция для цены книги в рублях"""
    price = randint(200, 1500)
    currency = "rub"
    return round(price),currency
    

def task_rating():
    """Функция для генарации рейтинга книги"""
    rating = triangular(1, 10)
    return round(rating)



def book_generator():
    pk = 1
    while True:
        yield {
            "model": MODEL,
            #"pk": next(pk()),
            "fields": {
                       "title": task_title(),
                       "year": task_year(),
                       "pages": task_pages(),
                       "isbn13": task_isbn(),
                       "rating": (task_rating()),
                       "price": task_price(),
                       "author": task_author()
                       }
            }
print(list(book_generator()))

def main():
    current_book_list = book_generator()
    books = [next(current_book_list) for _ in range(100)]
    with open('Book_list.json', 'w', encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

        
        
    








    


# Словарь
# if __name__ == "__main__":


