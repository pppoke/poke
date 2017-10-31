__Author__ = "Gamebu"

import pika
import time
import sys


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(3)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("method.delivery_tag", method.delivery_tag)
    print("consume end")

cred_broker = pika.PlainCredentials("admin", "123456")
conn_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    # virtual_host="/",
    # credentials=cred_broker
)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

# 声明
channel.exchange_declare(
    exchange='top_log',
    exchange_type='topic',
    durable=True,
)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

topics = sys.argv[1:]
if not topics:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for topic in topics:
    channel.queue_bind(
        queue=queue_name,
        exchange='top_log',
        routing_key=topic
    )

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    callback,
    queue=queue_name,
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
