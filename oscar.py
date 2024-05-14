from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import paho.mqtt.client as mqtt

class ControlPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.temp_label = Label(text="Temperatura: --")
        self.add_widget(self.temp_label)

        self.humidity_label = Label(text="Humedad: --")
        self.add_widget(self.humidity_label)

        self.color_label = Label(text="Color Hojas: --")
        self.add_widget(self.color_label)

        self.motor_label = Label(text="Motor Agua: --")
        self.add_widget(self.motor_label)

        self.client = mqtt.Client(protocol=mqtt.MQTTv311)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.connect("test.mosquitto.org", 1883, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conectado al broker")
            self.client.subscribe([
                ("planta/temperatura", 0),
                ("planta/humedad", 0),
                ("planta/color_hojas", 0),
                ("planta/motor_agua", 0)
            ])
        else:
            print(f"Error de conexión: {rc}")

    def on_disconnect(self, client, userdata, rc):
        print(f"Desconectado del broker. Código de retorno: {rc}")

    def on_message(self, client, userdata, msg):
        if msg.topic == "planta/temperatura":
            self.temp_label.text = f"Temperatura: {msg.payload.decode()}"
        elif msg.topic == "planta/humedad":
            self.humidity_label.text = f"Humedad: {msg.payload.decode()}"
        elif msg.topic == "planta/color_hojas":
            self.color_label.text = f"Color Hojas: {msg.payload.decode()}"
        elif msg.topic == "planta/motor_agua":
            self.motor_label.text = f"Motor Agua: {msg.payload.decode()}"

class MyApp(App):
    def build(self):
        return ControlPanel()

if __name__ == '__main__':
    MyApp().run()
