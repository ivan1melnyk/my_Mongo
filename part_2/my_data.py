import urllib.parse
from pymongo.server_api import ServerApi


# Створюємо рядок підключення з закодованими ім'ям користувача та паролем
connection_string = "mongodb+srv://melnykivan20a:<password>@ivan20a.c0mc4dz.mongodb.net/"

if '__main__' == __name__:
    from pymongo.mongo_client import MongoClient

    # Create a new client and connect to the server
    client = MongoClient(connection_string, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
