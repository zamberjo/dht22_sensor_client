
# DHT22 Sensor client for RPi


Installation
-------

I always recommend using virtualenv
```
apt-get update && apt-get install -y virtualenv build-essential python-dev python-openssl
```

```
git clone https://github.com/zamberjo/dht22_sensor_client.git /opt/dht22_sensor_client && pushd $_
```

```
virtualenv venv
source venv/bin/activate
```

```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git /opt/Adafruit && pushd $_
python setup.py install
popd
rm -rf /opt/Adafruit
```

```
pip install -r requeriments.txt
```

Use
---

Publish temperature and humidity
```
/opt/dht22_sensor_client/venv/bin/python dht22_cron.py
```

Crontab
-------

```
crontab -e
*/5 * * * * cd /opt/dht22_sensor_client/venv/bin/python /opt/dht22_sensor_client/dht22.py >/dev/null 2>&1
```
