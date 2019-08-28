import paho.mqtt.client as mqtt
from datetime import datetime
import plotly.graph_objects as go

import requests
from ubidots_handler.Config import Config as conf, Config
import pandas as pd
import json



'''
GLOBAL Variables
'''
value_list =[]


def on_connect(mqttc, obj, flags, rc):
    print("[INFO] Connected!")
    topic = "{}/{}/{}/lv".format(conf.TOPIC, conf.DEVICE_LABEL, conf.VARIABLE_LABEL)
    print(topic)
    mqttc.subscribe(topic, 0)

def on_message(mqttc, obj, msg):
    # Retrieving data
    value = conf.variable.get_values(1)[0]

    voulme = value.get("value")
    timestamp = value.get("timestamp")
    date = format(datetime.fromtimestamp(timestamp / 1000).strftime("%H:%M:%S"))

    # Unix epoch format
    #print("Value: {0}".format(voulme))
    #print("Timestamp: {0}".format(timestamp))
    #print("Date: {0}".format(date))

    #value_list.append({"value: ", value}, {"voulme: ", voulme}, {"timestamp: ", timestamp}, {"date: ", date})
    #print(value_list["value"])

    # Getting all the values from the server.
    value_list = get_values(device_label=conf.DEVICE_LABEL, var_label=conf.VARIABLE_LABEL, items=1000000000000000000000000)
    print(value_list)

def on_publish(mqttc, obj, mid):
    print("[INFO] Published!")


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("[INFO] Subscribed!")


def on_log(mqttc, obj, level, string):
    print("[INFO] Log info: {}".format(string))


"""
Get values from variable 
"""


def get_values(device_label, var_label, items):
    base_url = "http://things.ubidots.com/api/v1.6/devices/" + device_label + "/" + var_label + "/values"
    try:
        r = requests.get(base_url + '?token=' + conf.MQTT_USERNAME + "&page_size=" + str(items), timeout=20)

        return pd.io.json.json_normalize(r.json()["results"])
    except Exception as e:
        print(e)
        return {'error': 'Request failed or timed out'}


def get_last_sample():
    full_volume_list = get_values(device_label=conf.DEVICE_LABEL, var_label=conf.VARIABLE_LABEL,
                                  items=1000000000000000000000000)
    first_list = []
    curr_val = full_volume_list['volume'].loc[0]
    found = False
    counter = 0
    for val in full_volume_list['volume'][0:]:
        if val > curr_val:
            if counter == 0:
                first_list.append(curr_val)
                counter += 1
            first_list.append(val)
            found = True
        elif found:
            break
        curr_val = val
    return first_list


def main(conf):
    # Setup MQTT client
    mqttc = mqtt.Client()
    mqttc.username_pw_set(conf.MQTT_USERNAME, password=conf.MQTT_PASSWORD)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe


    # Uncomment to enable debug messages
    # mqttc.on_log = on_log

    mqttc.connect(conf.BROKER_ENDPOINT, conf.PORT, 60)
    topic = "{}/{}/{}/lv".format(conf.TOPIC, conf.DEVICE_LABEL, conf.VARIABLE_LABEL)
    print(topic)
    mqttc.subscribe(topic, 0)

    mqttc.loop_forever()

if __name__ == '__main__':
    conf = Config()
    main(conf)
    #print(get_last_sample())