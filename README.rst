

apt-get update && apt-get install -y virtualenv

cd /opt/
git clone git@github.com:zamberjo/THIS DHT22 && cd $_

virtualenv --clear venv
source venv/bin/activate

pip install -r requeriments.txt

crontab -e
*/5 * * * * cd /opt/DHT22/venv/bin/python /opt/DHT22/dht22.py >/dev/null 2>&1
