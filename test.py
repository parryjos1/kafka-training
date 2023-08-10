from kafka import KafkaProducer
import random
import time

# topic_name = "inputTopic3"
topic_name = "inputTopic4"

producer = KafkaProducer(
    bootstrap_servers="kafka-296bc5f1-hellofresh-b7c7.aivencloud.com:13794",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    security_protocol="SSL"
)

messages = [
    "welcome to kafka workshop",
    "Kafka is open sources distributed events steaming paltform",
    "kafka is highly scaleable",
    "hello world kafka",
    "I'm hungry what's for lunch"
]

while True:
    msg = random.choice(messages)
    message = msg.encode("UTF-8")
    print(message)
    producer.send(topic_name, key=b"key1", value=message)
    time.sleep(1)