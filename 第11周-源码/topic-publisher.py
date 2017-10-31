__Author__ = "Gamebu"

import pika
import time
import sys

cred_broker = pika.PlainCredentials("admin", "123456")
conn_params = pika.ConnectionParameters(host='localhost',
                                        #port=5672,
                                        #virtual_host="/",
                                        #credentials=cred_broker)
)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

# 声明
channel.exchange_declare(
    exchange='top_log',
    exchange_type='topic',
    durable=True,
)
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(
    exchange='top_log',
    routing_key=routing_key,
    body=message,
    properties=pika.BasicProperties(
                    delivery_mode=2,
                )
)
print("send message:", message)

connection.close()
