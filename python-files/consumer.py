#18th May 2023

#2. learn the print (f ) syntax
#3. Practise the % in print


import pika

#callback
def do_this (ch, method, props, body):
    print ("mesg is ",body)



#create connection params from pika
conn_params = pika.ConnectionParameters("localhost")

#create a connection
connection = pika.BlockingConnection(conn_params)

#create a channel
channel = connection.channel()

#set a queue to listen on
queue_name = 'mesg_for_Sanjay'
channel.queue_declare(queue = queue_name)

#consume the message
channel.basic_consume(queue=queue_name, on_message_callback=do_this,auto_ack=True)

channel.start_consuming()

connection.close

