import paho.mqtt.client as paho
from paho import mqtt
# from relay import set_relay
# from servo import set_servo

# define static variable
# broker = "localhost" # for local connection
broker = "industrial.api.ubidots.com"  # for online version
port = 1883
timeout = 60

#token device
username = 'BBFF-avT8OfD1uwsBcsmxjRRvaHGGzWMQHc'
password = 'BBFF-avT8OfD1uwsBcsmxjRRvaHGGzWMQHc'


# topic subscribe
pupuk_topic = '/v1.6/devices/relay/pupuk/lv' # -> contoh : /v1.6/devices/

 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(pupuk_topic)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    payload_decoded = msg.payload.decode('utf-8')

    if payload_decoded != '':

     if msg.topic == pupuk_topic:
        if float(payload_decoded) == 0.0:
            print("matikan relay")
            # set_relay("low")
        if float(payload_decoded) == 1.0:
            print("nyalakan relay")
           # set_relay("high")
        
# Create an MQTT client and attach our routines to it.
client = paho.Client()
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()

