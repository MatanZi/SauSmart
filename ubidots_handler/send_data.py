
import paho.mqtt.client as mqttClient
import time
import json
import random

from ubidots_handler.Config import Config

'''
global variables
'''

connected = False  # Stores the connection status


'''
Functions to process incoming and outgoing streaming
'''


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection

    else:
        print("[INFO] Error, connection failed")


def on_publish(client, userdata, result):
    print("[INFO] Published!")


def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0

        while not connected and attempts < 5:  # Waits for connection
            print("[INFO] Attempting to connect...")
            time.sleep(1)
            attempts += 1

    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True


def publish(mqtt_client, topic, payload):
    try:
        mqtt_client.publish(topic, payload)
    except Exception as e:
        print("[ERROR] There was an error, details: \n{}".format(e))


def main(mqtt_client ,ketchup_value ,conf):
    while ketchup_value > 0:

        choose = random.randint(1, 10)
        break_time = random.randint(1, 10)
        if choose < 6 and break_time < 3:
            for i in range(random.randint(3, 7)):
                time.sleep(1)
                sub = random.randint(1, 5)
                ketchup_value -= sub
                # Builds Payload and topíc
                payload = {conf.VARIABLE_LABEL: ketchup_value,
                           }
                payload = json.dumps(payload)
                topic = "{}{}".format(conf.TOPIC, conf.DEVICE_LABEL)

                if not connected:  # Connects to the broker
                    connect(mqtt_client, conf.MQTT_USERNAME, conf.MQTT_PASSWORD,
                            conf.BROKER_ENDPOINT, conf.PORT)

                # Publishes values
                print("[INFO] Attempting to publish payload:")
                print(payload)
                publish(mqtt_client, topic, payload)

        else:
            # Builds Payload and topíc
            payload = {conf.VARIABLE_LABEL: ketchup_value,
                      }
            payload = json.dumps(payload)
            topic = "{}{}".format(conf.TOPIC, conf.DEVICE_LABEL)

            if not connected:  # Connects to the broker
                connect(mqtt_client, conf.MQTT_USERNAME, conf.MQTT_PASSWORD,
                        conf.BROKER_ENDPOINT, conf.PORT)

            # Publishes values
            print("[INFO] Attempting to publish payload:")
            print(payload)
            publish(mqtt_client, topic, payload)



if __name__ == '__main__':
    conf = Config()
    mqtt_client = mqttClient.Client()
    ketchup = random.randint(80, 100)
    while True:
        main(mqtt_client, ketchup , conf)
        time.sleep(1)