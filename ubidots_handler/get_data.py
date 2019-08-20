'''
This Example sends harcoded data to Ubidots using the Paho MQTT
library.

Please install the library using pip install paho-mqtt

Made by Jose García @https://github.com/jotathebest/
Adapted from the original Paho Subscribe example at
https://github.com/eclipse/paho.mqtt.python/blob/master/examples/client_sub.py
'''

import paho.mqtt.client as mqtt
from ubidots import ApiClient
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
import requests


BROKER_ENDPOINT = "industrial.api.ubidots.com"
PORT = 1883
MQTT_USERNAME = "BBFF-zIOTwedsfKj84fXarZXHmdgJaAcSBT"  # Put here your TOKEN
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices"
DEVICE_LABEL = "sausmart"
VARIABLE_LABEL_1 = "volume"
api = ApiClient(token="BBFF-zIOTwedsfKj84fXarZXHmdgJaAcSBT")
variable = api.get_variable("5d5a91c573efc32748641b14")
value_list =[]



def on_connect(mqttc, obj, flags, rc):
    print("[INFO] Connected!")
    topic = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL_1)
    print(topic)
    mqttc.subscribe(topic, 0)

def on_message(mqttc, obj, msg):



    # Retrieving data
    value = variable.get_values(1)[0]
    #print("test")

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
    value_list = get_values(device_label=DEVICE_LABEL, var_label=VARIABLE_LABEL_1, items=1000000000000000000000000)

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
        r = requests.get(base_url + '?token=' + MQTT_USERNAME + "&page_size=" + str(items), timeout=20)
        return r.json()
    except Exception as e:
        print(e)
        return {'error': 'Request failed or timed out'}



def build_graph():
    value_list[""]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=value, y=df['AAPL.High'], name="AAPL High",
                             line_color='deepskyblue'))

    fig.add_trace(go.Scatter(x=df.Date, y=df['AAPL.Low'], name="AAPL Low",
                             line_color='dimgray'))

    fig.update_layout(title_text='Time Series with Rangeslider',
                      xaxis_rangeslider_visible=True)
    fig.show()

def main():
    my_specific_datasource = api.get_datasource('5d5a8e3a1d8472120bd6966d')
    # Get all variables
    all_variables = my_specific_datasource.get_variables()

    # Get last 10 variables
    some_variables = my_specific_datasource.get_variables(10)

    print(some_variables.get_items(3))
    print()
    # Setup MQTT client
    mqttc = mqtt.Client()
    mqttc.username_pw_set(MQTT_USERNAME, password="")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe


    # Uncomment to enable debug messages
    # mqttc.on_log = on_log

    mqttc.connect(BROKER_ENDPOINT, PORT, 60)
    topic = "{}/{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_LABEL_1)
    print(topic)
    mqttc.subscribe(topic, 0)

    mqttc.loop_forever()

if __name__ == '__main__':
    main()