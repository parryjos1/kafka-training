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

i=0

while i<1000000:
    ans = i%2

    if ans == 0:
        message = {"key": f"{ans}", "value": f"Even number {i} inserted in partition 0"}
    else:
        message = {"key": f"{ans}", "value": f"Odd number {i} inserted in partition 1"}

    print(message)
    # producer.send(topic_name, key=int(message["key"]), value=message["value"].encode("utf-8"))
    producer.send(topic_name, value=message["value"].encode("utf-8"), partition=int(message["key"]))
    print(ans)
    i = i + 1

