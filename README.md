
# DHT22 Sensor client for RPi


Installation
-------

I always recommend using virtualenv
```
apt-get update && apt-get install -y virtualenv
```

```
cd /opt/
git clone git@github.com:zamberjo/dht22_sensor_client.git dht22_sensor_client && cd $_
```

```
virtualenv venv
source venv/bin/activate
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
