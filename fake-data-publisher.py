from google.cloud import pubsub_v1
from faker import Faker
from faker.providers import internet
import time
import random

# TODO(developer)
project_id = "que-pacha-999"
topic_id = "ip-access"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 20):
     #Genera una parte entera y otra decimal para los milisegundos
    milisecs=random.randint(1,10)+random.random()
    fake = Faker()
    fake.add_provider(internet)
    data = fake.ipv4_private()
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)
    print(fake.ipv4_private())
    print(future.result())
    print(milisecs) 
    time.sleep(milisecs)  

print("Published messages.")





