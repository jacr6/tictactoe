# example_publisher.py
import pika, os, logging
logging.basicConfig()

class Publisher(object):
    def __init__(self) -> None:
        # Parse CLODUAMQP_URL (fallback to localhost)
        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
        self.params = pika.URLParameters(self.url)
        self.params.socket_timeout = 5
        self.connection = pika.BlockingConnection(self.params) # Connect to CloudAMQP
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue='pdfprocess') # Declare a queue
    
    # send a message
    def publish(self, msg):
        self.channel.basic_publish(exchange='', routing_key='pdfprocess', body=msg)
        print ("[x] Message sent to consumer")
        self.connection.close()