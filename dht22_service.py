# -*- coding: utf-8 -*-
# Jose Zambudio Bernabeu <zamberjo@gmail.com>

import paho.mqtt.client as mqtt
import logging

from sensor import SensorDHT22

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
# TODO: ... by config file
fileHandler = logging.FileHandler("dht22.log")
fileHandler.setFormatter(logFormatter)
_logger.addHandler(fileHandler)

# TODO: ... by config file
broker_address = "192.168.0.19"

# TODO: ... by config file
pin = 4


def on_message(client, userdata, msg):
    _logger.info("on_message %r | %r | %r", client, userdata, msg)
    _logger.info(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    sensor = SensorDHT22(pin)
    # TODO: ... by config file
    if msg.topic == "/house/office/temperature/request":
        response = sensor.read_temperature()
        _logger.info("/house/office/humidity -> %r", response)
        client.publish("/house/office/temperature", "%.2f" % (response))

    elif msg.topic == "/house/office/humidity/request":
        response = sensor.read_temperature()
        _logger.info("/house/office/temperature -> %r", response)
        client.publish("/house/office/humidity", "%.2f" % (response))

    elif msg.topic == "/house/office/sensors/request":
        response = sensor.read()
        _logger.info("/house/office/temperature -> %r", response)
        client.publish("/house/office/temperature", "%.2f" % (response[0]))

        _logger.info("/house/office/humidity -> %r", response)
        client.publish("/house/office/humidity", "%.2f" % (response[1]))


def on_connect(client, userdata, flags, rc):
    _logger.info("Connected with result code " + str(rc))
    # TODO: ... by config file
    client.subscribe("/house/office/temperature/request")
    client.subscribe("/house/office/humidity/request")
    client.subscribe("/house/office/sensors/request")


_logger.info("Starting client...")
client = mqtt.Client()
_logger.info("Cliente %r", client)
client.on_connect = on_connect
client.on_message = on_message
_logger.info("on_connect %r", on_connect)
_logger.info("on_message %r", on_message)

_logger.info("Connecting mqtt server...")
client.connect(broker_address)

client.loop_forever()
