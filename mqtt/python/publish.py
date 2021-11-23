import paho.mqtt.publish as publish
import random

topic = "random/int"
payload = random.randint(-100, 100)

publish.single(topic, payload, qos=0, retain=False, hostname="localhost", port=1883)

print("topic: " + topic + ", payload: " + str(payload))
