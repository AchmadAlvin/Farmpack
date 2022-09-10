import paho.mqtt.client as paho
from paho import mqtt

broker = "industrial.api.ubidots.com" 
port = 1883
timeout = 60

username = 'BBFF-avT8OfD1uwsBcsmxjRRvaHGGzWMQHc'
password = 'BBFF-avT8OfD1uwsBcsmxjRRvaHGGzWMQHc'


pupuk_topic = '/v1.6/devices/relay/pupuk/lv' 
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
   
    client.subscribe(pupuk_topic)
 
def on_message(client, userdata, msg):
    payload_decoded = msg.payload.decode('utf-8')

    if payload_decoded != '':

     if msg.topic == pupuk_topic:
        if float(payload_decoded) == 0.0:
            print("relay mati")
        if float(payload_decoded) == 1.0:
            print("relay nyala")
        

client = paho.Client()
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()

