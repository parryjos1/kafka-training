from kafka import KafkaConsumer

topic_name = "pizzaOrders"

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers="kafka-296bc5f1-hellofresh-b7c7.aivencloud.com:13794",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    security_protocol="SSL",
    auto_offset_reset="earliest"
)

for msg in consumer:
    message=msg.value.decode("UTF-8")
    print(message)