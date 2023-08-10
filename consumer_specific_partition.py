from kafka import KafkaConsumer, TopicPartition


consumer = KafkaConsumer(
    bootstrap_servers="kafka-296bc5f1-hellofresh-b7c7.aivencloud.com:13794",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    security_protocol="SSL",
    auto_offset_reset="earliest"
)
consumer.assign([TopicPartition("inputTopic2", 0), TopicPartition("inputTopic4", 1)])

for msg in consumer:
    message=msg.value.decode("UTF-8")
    print(message)