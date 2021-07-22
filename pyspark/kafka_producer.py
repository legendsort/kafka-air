from kafka import KafkaProducer
import csv
import time

topic = 'quickstart-events'
bootstrap_servers = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
reader = csv.DictReader(open("/Users/mehmeteraysurmeli/PycharmProjects/Django-/dataeng/mediadata.csv"))
for row in reader:
    print(row)
    msg = f'Kontext kafka msg: { row }'
    future = producer.send(topic, msg.encode('utf-8'))
    print(f'Sending msg: {msg}')
    result = future.get(timeout=60)
    time.sleep(1.0)


# for more understandable reading
"""
with open('/Users/mehmeteraysurmeli/PycharmProjects/Django-/dataeng/mediadata.csv', 'rt')as f:
    data = csv.reader(f)
    for row in data:
        print(row)
        msg = f'Kontext kafka msg: { row }'
        future = producer.send(topic, msg.encode('utf-8'))
        print(f'Sending msg: {msg}')
        result = future.get(timeout=60)
"""
metrics = producer.metrics()
print(metrics)
