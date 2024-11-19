import paho.mqtt.client as mqtt
import json

MQTT_BROKER = "broker.hivemq.com"
TOPIC = "healthcare/data"

# MQTT setup
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload}")

client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)

# Publishing simulated data
def publish_data(data):
    client.publish(TOPIC, json.dumps(data))
    print("Data published")

data = {'timestamp': '2024-11-19 12:00:00', 'heart_rate': 80, 'temperature': 36.7}
publish_data(data)
client.loop_start()
