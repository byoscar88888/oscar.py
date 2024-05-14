import paho.mqtt.client as mqtt
import random
import time

def publish_temperature(client):
    while True:
        temperature = random.uniform(15, 30)
        client.publish("planta/temperatura", temperature)
        print(f"Temperatura enviada: {temperature}")
        time.sleep(5)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        publish_temperature(client)
    else:
        print(f"Error de conexión: {rc}")

def on_disconnect(client, userdata, rc):
    print(f"Desconectado del broker. Código de retorno: {rc}")

client_temp = mqtt.Client("SensorTemperatura", protocol=mqtt.MQTTv311)
client_temp.on_connect = on_connect
client_temp.on_disconnect = on_disconnect

try:
    client_temp.connect("test.mosquitto.org", 1883, 60)
    client_temp.loop_forever()
except Exception as e:
    print(f"Excepción al conectar: {e}")
