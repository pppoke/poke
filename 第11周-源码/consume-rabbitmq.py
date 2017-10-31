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

# 声明queue
channel.queue_declare(queue='gamebu1', durable=True)
channel.queue_declare(queue='gamebu0', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    # time.sleep(3)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("method.delivery_tag", method.delivery_tag)
    time.sleep(30)
    print("consume end")


# channel.basic_consume(callback,
#                       queue='gamebu1',
#                       #no_ack=True
#                        )
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='gamebu0',
                      #no_ack=True
                       )
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()