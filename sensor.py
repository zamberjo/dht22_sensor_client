# -*- coding: utf-8 -*-
# Jose Zambudio Bernabeu <zamberjo@gmail.com>

import Adafruit_DHT


class SensorDHT22():
    def __init__(self, pin, sensor=None):
        self.pin = pin
        self.sensor = sensor or Adafruit_DHT.DHT22

    def read_humidity(self):
        """
        Read humidity

        :return: Humidity value
        :rtype: Float
        """
        return Adafruit_DHT.read_retry(self.sensor, self.pin)[0]

    def read_temperature(self):
        """
        Read Temperature

        :return: Temperature value
        :rtype: Float
        """
        return Adafruit_DHT.read_retry(self.sensor, self.pin)[1]

    def read(self):
        """
        Read humidity and temperature from sensor

        :return: tuple (humidity, temperature) of floats
        :rtype: tuple
        """
        return Adafruit_DHT.read_retry(self.sensor, self.pin)
