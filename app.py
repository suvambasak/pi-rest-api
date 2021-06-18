import flask
from flask import request, jsonify, render_template
from werkzeug.wrappers import response
from datetime import datetime

from sensors import DHT

app = flask.Flask(__name__)
DHT_sensor = DHT(4)


def get_timedata():
    time_date = datetime.now()
    return time_date.strftime("%H:%M:%S"), time_date.strftime("%d/%m/%Y")


@app.route('/api/v1/led/status', methods=['GET'])
def led_status():
    response = dict()
    response['time'], response['date'] = get_timedata()
    response['status'] = 'OFF'
    return jsonify(response)


@app.route('/api/v1/dht/temperature', methods=['GET'])
def dht_temp():
    response = dict()
    response['time'], response['date'] = get_timedata()

    DHT_sensor.sense()
    response['temperature'] = DHT_sensor.get_temperature()
    return jsonify(response)


@app.route('/api/v1/dht/humidity', methods=['GET'])
def dht_hum():
    response = dict()
    response['time'], response['date'] = get_timedata()

    DHT_sensor.sense()
    response['humidity'] = DHT_sensor.get_humidity()
    return jsonify(response)


@app.route('/api/v1/dht', methods=['GET'])
def dht_all():
    response = dict()
    response['time'], response['date'] = get_timedata()

    DHT_sensor.sense()
    response['humidity'] = DHT_sensor.get_humidity()
    response['temperature'] = DHT_sensor.get_temperature()
    return jsonify(response)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
