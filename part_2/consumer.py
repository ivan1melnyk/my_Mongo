import pika

import json
import pymongo
from my_data import connection_string

client = pymongo.MongoClient(connection_string)
db = client.mydatabase
collection = db.contact

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def sent_email_massege(message):
    print(message['name'])
    query = {"name": message['name']}
    update = {"$set": {"is_sent": True}}
    collection.update_one(query, update, upsert=True)


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")

    sent_email_massege(message)

    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
