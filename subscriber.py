import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "samay/module3/demo"

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to broker!")

    result, mid = client.subscribe(TOPIC)
    print("Subscribe result:", result)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print("\nReceived:")
    print(json.dumps(data, indent=4))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Waiting for messages...")
client.loop_forever()