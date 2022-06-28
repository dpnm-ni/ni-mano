# -*- coding: utf-8 -*-
import argparse
import sys
import json
import pdb
import logging

from ni_collector.extractors import collectd
from ni_collector.extractors import generic
from ni_collector.config import cfg

from influxdb import InfluxDBClient

from flask import Flask, request, Response


logger = logging.getLogger(__name__)

app = Flask(__name__)

influxdb_cfg = cfg['influxdb']
influxdb_client = InfluxDBClient(host=influxdb_cfg['server'],
                                 database=influxdb_cfg['database'])
influxdb_client.create_database(influxdb_cfg['database'])
influxdb_client.create_retention_policy(name="infinite",
                                        duration='INF',
                                        replication=1,
                                        database=influxdb_cfg['database'],
                                        default=True
                                        )


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        logger.error('Message delivery failed: {}'.format(err))


def store_measurements(measurements):
    # Send extracted data to influxdb
    influxdb_data_points = []
    for item in measurements:
        influxdb_data_points.append({"measurement": item[0],
                                     # timestamp from ms in collectd to ns in influxdb
                                     "time": int(item[2]) * 10**6,
                                     "fields": {"value": item[1], }
                                     })
    influxdb_client.write_points(influxdb_data_points)


@app.route('/collectd', methods=['POST'])
def recv_collectd_data():
    measurements = []
    for data in request.json:
        measurements.extend(collectd.get_measurements(data))
    store_measurements(measurements)
    return Response(status=200)


@app.route('/', methods=['POST'])
def recv_generic_data():
    measurements = []
    for data in request.json:
        measurements.extend(generic.get_measurements(data))
    store_measurements(measurements)
    return Response(status=200)

def main():
    app.run(host='0.0.0.0', port=8401)


if __name__ == '__main__':
    main()
