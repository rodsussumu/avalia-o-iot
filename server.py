#!/usr/bin/env python3

from influxdb import InfluxDBClient
from flask import Flask, request
import logging
import datetime

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return 'API is up!'

def shouldIrrigate(soil_humidity):
    if soil_humidity > 800:
        return True
    if soil_humidity < 800:
        return False

@api.route('/api/v1/metric', methods=['POST'])
def create():
    data = request.get_json()
    soil_humidity = data['soil_humidity']
    luminosidade = data['luminosidade']
    air_humidity = data['air_humidity']
    air_temp = data['air_temp']

    resp = False

    if (soil_humidity > 800) and (luminosidade > 500) :
        resp = True
        payload = [
            {
                "measurement": "smart_garden",
                "tags": {
                    "name": "metricas"
                },
                "time": datetime.datetime.utcnow().isoformat(),
                "fields": {
                    "soil_humidity": int(soil_humidity),
                    "luminosidade": int(luminosidade),
                    "air_humidity": air_humidity,
                    "air_temp": air_temp,
                    "shouldIrrigate": resp
                }
            }
        ]

    if (soil_humidity > 800) and (luminosidade < 500):
        resp = False
        payload = [
            {
                "measurement": "smart_garden",
                "tags": {
                    "name": "metricas"
                },
                "time": datetime.datetime.utcnow().isoformat(),
                "fields": {
                    "soil_humidity": int(soil_humidity),
                    "luminosidade": int(luminosidade),
                    "air_humidity": air_humidity,
                    "air_temp": air_temp,
                    "shouldIrrigate": resp
                }
            }
        ]

    influx_cliente = InfluxDBClient('influxdb', 8086, database='smart_garden')
    influx_cliente.write_points(payload)
    
    stringResp = "Não irrigar" if resp == False else "Irrigar"
    return '{resp}, {stringResp}'.format(resp=resp, stringResp=stringResp)

    

if __name__ == '__main__':
    api.run(host='0.0.0.0', debug=True, port=3000)