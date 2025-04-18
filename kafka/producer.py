# Simulates POS data and pushes it to Kafka
from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

items = ['apple', 'banana', 'shirt', 'book', 'pen']
categories = ['food', 'clothing', 'stationery']

while True:

    data = {
        'store_id': random.randint(1, 5),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'item': random.choice(items),
        'category': random.choice(categories),
        'quantity': random.randint(1, 5),
        'price': round(random.uniform(1.0, 100.0), 2)
    }
    producer.send('retail_sales', value=data)
    print(f"Sent: {data}")
    time.sleep(1)