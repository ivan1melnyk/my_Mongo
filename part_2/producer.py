import pika

from datetime import datetime
import json
from model import Contact
from faker import Faker
from my_data import connection_string
from mongoengine import connect


connect('mydatabase', host=connection_string)

fake = Faker()


def fake_email():
    fake_email = f'{fake.name().lower().split(" ")[1]}.143@gmail.com'
    return fake_email


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')


def main():
    contacts = list()
    for i in range(5):
        contact = Contact(name=fake.name(), email=fake_email())
        contact.save()

        print('contact.id', str(contact.id))

        message = {
            "id": i+1,
            "name": contact.name,
            "email": contact.email,
            "date": datetime.now().isoformat()
        }

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
    connection.close()


if __name__ == '__main__':
    main()
