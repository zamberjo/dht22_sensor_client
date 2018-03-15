# -*- coding: utf-8 -*-
# Jose Zambudio Bernabeu <zamberjo@gmail.com>

import paho.mqtt.client as mqtt
import logging

from sensor import SensorDHT22

_logger = logging.getLogger(__name__)

logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
# TODO: ... by config file
fileHandler = logging.FileHandler("dht22.log")
fileHandler.setFormatter(logFormatter)
_logger.addHandler(fileHandler)

# TODO: ... by config file
broker_address = "192.168.0.19"


def on_message(mosq, obj, msg):
    _logger.info("on_message %r | %r | %r", mosq, obj, msg)
    _logger.info(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    sensor = SensorDHT22()
    # message = msg.payload
    client = mqtt.Client()
    client.connect(broker_address)
    client.loop_start()
    # TODO: ... by config file
    if msg.topic == "house/office/temperature/request":
        response = sensor.read_temperature()
        client.publish("/house/office/temperature", "%.2f" % (response))
    elif msg.topic == "house/office/humidity/request":
        response = sensor.read_temperature()
        client.publish("/house/office/humidity", "%.2f" % (response))
    elif msg.topic == "house/office/sensors/request":
        response = sensor.read()
        client.publish("/house/office/temperature", "%.2f" % (response[0]))
        client.publish("/house/office/humidity", "%.2f" % (response[1]))
    client.loop_stop()

client = mqtt.Client()
client.on_message = on_message
# TODO: ... by config file
client.subscribe("house/office/temperature/request")
client.subscribe("house/office/humidity/request")
client.subscribe("house/office/sensors/request")
client.connect(broker_address)

client.loop_forever()
