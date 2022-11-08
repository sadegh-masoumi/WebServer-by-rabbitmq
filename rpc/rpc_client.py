import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials("myuser", "mypassword")
        parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        self.connection = connection

        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="test_queue")
        self.channel.queue_bind(exchange="e1", queue="test_queue", routing_key="rk1")

        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="e1",
            routing_key="rk",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n),
        )
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)
