#Source: https://stackoverflow.com/questions/53706451/attributeerror-module-pika-has-no-attribute-blockingconnection-error-in-rab
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                  routing_key='hello',
                  body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()