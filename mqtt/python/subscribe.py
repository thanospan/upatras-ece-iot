import paho.mqtt.subscribe as subscribe

def print_msg(client, userdata, message):
  print("topic: %s, payload: %s" % (message.topic, message.payload))

topics = ["#"]

print("---Waiting for messages---")

subscribe.callback(print_msg, topics, qos=0, hostname="localhost", port=1883)
