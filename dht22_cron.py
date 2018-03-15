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

# TODO: ... by config file
pin = 4

client = mqtt.Client()
client.connect(broker_address)

client.loop_start()
sensor = SensorDHT22(pin)

humidity, temperature = sensor.read()
# TODO: ... by config file
client.publish("/house/office/temperature", "%.2f" % (temperature))
client.publish("/house/office/humidity", "%.2f" % (humidity))
_logger.info("HUMIDITY {} | TEMPERATURE {}" .format(humidity, temperature))

client.loop_stop()
