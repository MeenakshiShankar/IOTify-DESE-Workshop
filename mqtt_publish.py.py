import random
import time
import json
 
from paho.mqtt import client as mqtt_client
from serial import Serial
 
serial_data = Serial('com10',115200)
 
 
#broker = '10.114.241.62'
broker = "broker.hivemq.com"
port = 1883
topic_fft = "workshop/motor/fft"
topic_current = "workshop/motor/current"
topic_airlock = "workshop/motor/airlock"
topic_stability = "workshop/motor/stability"
topic_stalling = "workshop/motor/stalling"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'Emqx'
password = 'password'
 
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
 
    client = mqtt_client.Client(client_id,clean_session=False)
    client.username_pw_set(username, password)
    client.will_set("will_topic", "disconnected", 1, True)
    client.on_connect = on_connect
    client.connect(broker, port)
 
    return client
 
 
def publish(client):
   
    count = 0
 
    while True:
        time.sleep(1)
        #current_data = serial_data.readline()
        ##airlock_data=random.randint(0,100)
        rand_list=[]
        for i in range(68):
         rand_list.append(int(serial_data.readline()))
        current_data = rand_list[64]
        airLock = rand_list[65]
        Stability = rand_list[66]
        Stalling = rand_list[67]
        ##fft_data = json.dumps(rand_list)
 
       
        #msg = data
 
        count = count+1
        print(count)
 
       
        ###### CURRENT DATA ############
       
        result = client.publish(topic_current, current_data,2,True)
        status = result[0]
        if status == 0:
            print(f"Sent Current Reading {current_data} to topic `{topic_current}`")
        else:
            print(f"Failed to send message to topic {topic_current}")
 
        #### AIRLOCK #########
        result = client.publish(topic_airlock, airLock,2,True)
        status = result[0]
        if status == 0:
            print(f"Sent AirLock {airLock} to topic `{topic_airlock}`")
        else:
            print(f"Failed to send message to topic {topic_airlock}")
 
        #### STABILITY #########
        result = client.publish(topic_stability, Stability,2,True)
        status = result[0]
        if status == 0:
            print(f"Sent Stability {Stability} to topic `{topic_stability}`")
        else:
            print(f"Failed to send message to topic {topic_stability}")
       
        #### STALLING #########
        result = client.publish(topic_stalling, Stalling,2,True)
        status = result[0]
        if status == 0:
            print(f"Sent Stalling {Stalling} to topic `{topic_stalling}`")
        else:
            print(f"Failed to send message to topic {topic_stalling}")
 
         ######   FFT ###############      
        for i in range(4):
            rand_list[64+i] = 0
        fft_data = json.dumps(rand_list)
 
        result = client.publish(topic_fft, fft_data,2,True)
        status = result[0]
        if status == 0:
            print(f"Sent fft {fft_data} to topic `{topic_fft}`")
        else:
            print(f"Failed to send message to topic {topic_fft}")
 
 
       
 
 
 
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
 
 
if __name__ == '__main__':
    run()
 