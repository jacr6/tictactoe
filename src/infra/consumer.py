# example_consumer.py
import pika, os, time

class Consumer(object):
    def __init__(self) -> None:
        pass
        # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
        self.params = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue='pdfprocess') # Declare a queue
        
    def consume(self):
        # set up subscription on the queue
        self.channel.basic_consume('pdfprocess',
        self.callback,
        auto_ack=True)
        # start consuming (blocks)
        self.channel.start_consuming()
        self.connection.close()
    
    def pdf_process_function(msg):
        print(" PDF processing")
        print(" [x] Received " + str(msg))

        time.sleep(5) # delays for 5 seconds
        print(" PDF processing finished")
        return

    # create a function which is called on incoming messages
    def callback(self, ch, method, properties, body):
        self.pdf_process_function(body)

