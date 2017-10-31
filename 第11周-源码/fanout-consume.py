__Author__ = "Gamebu"

import pika
import time
import gevent

cred_broker = pika.PlainCredentials("admin", "123456")
conn_params = pika.ConnectionParameters(host='localhost',
                                        port=5672,
                                        # virtual_host="/",
                                        # credentials=cred_broker
)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

# 声明
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout',
    durable=True,
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(queue=queue_name, exchange='logs')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(3)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("method.delivery_tag", method.delivery_tag)
    print("consume end")


# channel.basic_consume(callback,
#                       queue='gamebu1',
#                       #no_ack=True
#                        )
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name,
)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()