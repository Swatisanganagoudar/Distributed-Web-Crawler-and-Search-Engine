import pika
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import hashlib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

visited = set()
SAVE_FOLDER = "pages"
os.makedirs(SAVE_FOLDER, exist_ok=True)

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
channel.queue_declare(queue='crawler_queue')

def callback(ch, method, properties, body):
    url = body.decode()

    if url in visited:
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    print("Processing:", url)

    try:
        response = requests.get(url, timeout=5,verify=False)
        if response.status_code == 200:
            
            # Save HTML file
            filename = hashlib.md5(url.encode()).hexdigest() + ".html"
            filepath = os.path.join(SAVE_FOLDER, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(response.text)

            print("Saved:", filename)

            # Extract links
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a", href=True):
                new_url = urljoin(url, link["href"])

                if urlparse(new_url).scheme in ["http", "https"]:
                    channel.basic_publish(
                        exchange='',
                        routing_key='crawler_queue',
                        body=new_url
                    )

            visited.add(url)

    except Exception as e:
        print("Error:", e)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue='crawler_queue',
    on_message_callback=callback
)

print("Worker started. Waiting for URLs...")
channel.start_consuming()