import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "samay/module3/demo"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(BROKER, PORT, 60)

result = client.publish(TOPIC, "hello")

client.loop(1)

print("Publish result:", result.rc)

client.disconnect()