import pika

# Seed URLs
seed_urls = [
    "https://example.com",
    "https://www.wikipedia.org"
]

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Create queue
channel.queue_declare(queue='crawler_queue')

for url in seed_urls:
    channel.basic_publish(
        exchange='',
        routing_key='crawler_queue',
        body=url
    )
    print("Sent:", url)

connection.close()