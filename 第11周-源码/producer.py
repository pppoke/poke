__Author__ = "Gamebu"

import pika
import time

cred_broker = pika.PlainCredentials("admin", "123456")
conn_params = pika.ConnectionParameters(host='172.16.2.146',
                                        port=5672,
                                        #virtual_host="/",
                                        credentials=cred_broker)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

# 声明queue

channel.queue_declare(queue='gamebu')

channel.basic_publish(exchange='',
                    routing_key='gamebu',
                    body='Hello,Gamebu!')

print("Send End")

connection.close()