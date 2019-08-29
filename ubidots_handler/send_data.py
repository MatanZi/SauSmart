import paho.mqtt.client as mqttClient
import time
import json
import random
from ubidots_handler.Config import Config

'''
global variables
'''

connected = False  # Stores the connection status
BROKER_ENDPOINT = "industrial.api.ubidots.com"
PORT = 1883
MQTT_USERNAME = "BBFF-zIOTwedsfKj84fXarZXHmdgJaAcSBT"  # Put here your TOKEN
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "sausmart"
VARIABLE_LABEL_1 = "volume"

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


def main(mqtt_client, value, type, conf):
        while value > 0:
            if type_value <= 3:
                choose = random.randint(1, 10)
                break_time = random.randint(1, 10)
                if choose < 6 and break_time < 3:
                    for i in range(random.randint(3, 7)):
                        time.sleep(1)
                        add = random.randint(1, 5)
                        value += add
                        if value <= 0:
                            break
                        else:
                            # Builds Payload and topíc
                            payload = {VARIABLE_LABEL_1: value
                                       }
                            payload = json.dumps(payload)
                            topic = "{}{}".format(TOPIC, DEVICE_LABEL)

                            if not connected:  # Connects to the broker
                                connect(mqtt_client, MQTT_USERNAME, MQTT_PASSWORD,
                                        BROKER_ENDPOINT, PORT)

                            # Publishes values
                            print("[INFO] Attempting to publish payload:")
                            print(payload)
                            publish(mqtt_client, topic, payload)

            elif type_value < 6 and type_value > 3:
                choose = random.randint(1, 10)
                break_time = random.randint(1, 10)
                if choose < 3 and break_time < 3:
                    for i in range(random.randint(3, 7)):
                        time.sleep(1)
                        add = random.randint(1, 5)
                        value += add
                        if value <= 0:
                            break

                        else:
                            # Builds Payload and topíc
                            payload = {VARIABLE_LABEL_1: value
                                       }
                            payload = json.dumps(payload)
                            topic = "{}{}".format(TOPIC, DEVICE_LABEL)

                            if not connected:  # Connects to the broker
                                connect(mqtt_client, MQTT_USERNAME, MQTT_PASSWORD,
                                        BROKER_ENDPOINT, PORT)

                            # Publishes values
                            print("[INFO] Attempting to publish payload:")
                            print(payload)
                            publish(mqtt_client, topic, payload)

            elif type_value == 6:
                choose = random.randint(1, 10)
                break_time = random.randint(1, 10)
                if choose < 3 and break_time < 2:
                    for i in range(random.randint(3, 7)):
                        time.sleep(1)
                        add = random.randint(1, 5)
                        value += add
                        if value <= 0:
                            break

                        else:
                            # Builds Payload and topíc
                            payload = {VARIABLE_LABEL_1: value
                                       }
                            payload = json.dumps(payload)
                            topic = "{}{}".format(TOPIC, DEVICE_LABEL)

                            if not connected:  # Connects to the broker
                                connect(mqtt_client, MQTT_USERNAME, MQTT_PASSWORD,
                                        BROKER_ENDPOINT, PORT)

                            # Publishes values
                            print("[INFO] Attempting to publish payload:")
                            print(payload)
                            publish(mqtt_client, topic, payload)



if __name__ == '__main__':
    conf = Config()
    mqtt_client = mqttClient.Client()
    while True:
        type_value = random.randint(1, 6)
        value = random.randint(5, 20)
        main(mqtt_client, value, type_value, conf)
        time.sleep(1)
