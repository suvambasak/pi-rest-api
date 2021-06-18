import datetime
import flask
from flask import request, jsonify, render_template
from werkzeug.wrappers import response
from datetime import datetime

app = flask.Flask(__name__)


@app.route('/api/v1/led/status', methods=['GET'])
def led_status():
    response = dict()
    response['date'] = datetime.now().strftime("%d/%m/%Y")
    response['time'] = datetime.now().strftime("%H:%M:%S")
    response['status'] = 'OFF'
    return jsonify(response)


@app.route('/api/v1/dht/temperature', methods=['GET'])
def dht_temp():
    response = dict()
    response['date'] = datetime.now().strftime("%d/%m/%Y")
    response['time'] = datetime.now().strftime("%H:%M:%S")
    response['temperature'] = '33.3'
    return jsonify(response)


@app.route('/api/v1/dht/humidity', methods=['GET'])
def dht_hum():
    response = dict()
    response['date'] = datetime.now().strftime("%d/%m/%Y")
    response['time'] = datetime.now().strftime("%H:%M:%S")
    response['humidity'] = '50.6%'
    return jsonify(response)


@app.route('/api/v1/dht', methods=['GET'])
def dht_all():
    response = dict()
    response['date'] = datetime.now().strftime("%d/%m/%Y")
    response['time'] = datetime.now().strftime("%H:%M:%S")
    response['humidity'] = '53.6%'
    response['temperature'] = '30.3'
    return jsonify(response)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
