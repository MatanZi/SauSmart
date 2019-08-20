from ubidots import ApiClient

class Config():
    def __init__(self):
        self.BROKER_ENDPOINT = "industrial.api.ubidots.com"
        self.PORT = 1883
        self.MQTT_USERNAME = "BBFF-zIOTwedsfKj84fXarZXHmdgJaAcSBT"  # Put here your TOKEN
        self.MQTT_PASSWORD = ""
        self.TOPIC = "/v1.6/devices"
        self.DEVICE_LABEL = "sausmart"
        self.VARIABLE_LABEL = "volume"
        self.api = ApiClient(token="BBFF-zIOTwedsfKj84fXarZXHmdgJaAcSBT")
        self.variable = self.api.get_variable("5d5a91c573efc32748641b14")