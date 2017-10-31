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

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='gamebu',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()