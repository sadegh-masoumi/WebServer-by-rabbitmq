import pika

credentials = pika.PlainCredentials("myuser", "mypassword")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange="e1", durable="true", exchange_type="direct")
channel.queue_declare(queue="test_queue_2")
channel.queue_bind(exchange="e1", queue="test_queue_2", routing_key="rk")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n + 30)
    print(f"server (without response) - {response}")

    ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="test_queue_2", on_message_callback=on_request)
print(" [x] Awaiting RPC requests")
channel.start_consuming()
