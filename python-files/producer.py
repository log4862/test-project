#17th May 2023

import os
import pika

connection_params = pika.ConnectionParameters ('localhost')

#make a connection 
connection = pika.BlockingConnection(connection_params)

#get a channel from that connection (i.e. one postman)
channel = connection.channel()

queue_name = 'mesg_for_Sanjay'

# declare a queue on the channel
channel.queue_declare(queue = queue_name)

channel.basic_publish(exchange='', routing_key=queue_name, body='this_mesg came from my own queue')

#while i <5 :
    #publish the mesg
 ##  channel.basic_publish(exchange='', routing_key=queue_name, body=this_mesg)
   # i = i+1

print ("sent mesg")

connection.close
