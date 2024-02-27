from models import Author, Quote
from my_data import connection_string
import sys
import json
from mongoengine import connect


connect('mydatabase', host=connection_string)


# Функція для завантаження даних з файлу authors.json
def load_authors_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        # result_authors = db.mydatabase.insert_many(authors_data)
        for author in authors_data:
            author_record = Author(fullname=author["fullname"], born_date=author["born_date"],
                                   born_location=author["born_location"], description=author["description"])
            author_record.save()


# Функція для завантаження даних з файлу quotes.json
def load_quotes_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        # result_quotes = db.mydatabase.insert_many(quotes_data)
        for quote in quotes_data:
            quote_record = Quote(
                tags=quote['tags'], author=quote['author'], quote=quote['quote'])
            quote_record.save()


# Завантаження даних з файлів у базу даних
load_authors_from_json('json/authors.json')
load_quotes_from_json('json/quotes.json')
