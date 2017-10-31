__Author__ = "Gamebu"

import pika
import time

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
    exchange='logs',
    exchange_type='fanout',
    durable=True,
)

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body='Hello,Gamebu哇的0'.encode(),
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)
print("Send Hello,Gamebu哇的")
# time.sleep(2)
print("Send End")

connection.close()