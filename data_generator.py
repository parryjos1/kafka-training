import json

from kafka import KafkaProducer
import random
import time

topic_name = "pizzaOrders"

producer = KafkaProducer(
    bootstrap_servers="kafka-296bc5f1-hellofresh-b7c7.aivencloud.com:13794",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
    security_protocol="SSL"
)

# Different types of orders
order_type = [
    "Dine-in",
    "Takeaway",
    "Delivery",
    "Curbside Pickup",
    "Express Lunch",
    "Family Feast",
    "Date Night Special",
    "Solo Indulgence",
    "Office Party Pack",
    "Late Night Snack"
]

# Names for different pizza varieties
order_name = [
    "The Classic Margherita",
    "Sizzling Pepperoni",
    "Hawaiian Dream",
    "BBQ Chicken Bonanza",
    "Veggie Delight",
    "Mushroom Mania",
    "Spicy Buffalo Blast",
    "Seafood Extravaganza",
    "Four Cheese Heaven",
    "Tantalizing Taco Pizza"
]

# Different toppings
toppings = [
    "Extra Cheese",
    "Sun-Dried Tomatoes",
    "Pineapple & Ham",
    "Fresh Basil",
    "Roasted Garlic",
    "Sliced Olives",
    "Spicy Jalapenos",
    "Sweet Corn",
    "Crispy Bacon",
    "Grilled Chicken"
]

i=0

while True:
    message={
        "order_id": f"{i}",
        "order_type": f"{random.choice(order_type)}",
        "pizza_name": f"{random.choice(order_name)}",
        "topping": f"{random.choice(toppings)}",
        "order_size": f"{random.randint(2, 6)}"
    }
    print(message)
    message_json = json.dumps(message)
    msg = message_json.encode("UTF-8")
    producer.send(topic_name, value=msg)
    i = i + 1
    time.sleep(1)
