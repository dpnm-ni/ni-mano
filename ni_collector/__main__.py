# -*- coding: utf-8 -*-
import argparse
import sys
import json
import pdb
import logging

from ni_collector import metric_extractor
from ni_collector.config import cfg

from confluent_kafka import Producer
from influxdb import InfluxDBClient

from flask import Flask, request, Response


logger = logging.getLogger(__name__)

app = Flask(__name__)

producer = Producer(cfg['kafka_producer'])

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


@app.route('/', methods=['POST'])
def recv_mon_data():
    measurements = []
    influxdb_data_points = []
    for data in request.json:
        measurements.extend(metric_extractor.get_measurements(data))

    # Send extracted data to kafka topics
    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    for item in measurements:
        producer.produce(topic='ni',
                         value=str({item[0]: item[1]}),
                         timestamp=int(item[2]),
                         callback=delivery_report)
        producer.poll(0)

    # Send extracted data to influxdb
    for item in measurements:
        influxdb_data_points.append({"measurement": item[0],
                                     # timestamp from ms in collectd to ns in influxdb
                                     "time": int(item[2]) * 10**6,
                                     "fields": {"value": item[1], }
                                     })
    influxdb_client.write_points(influxdb_data_points)

    return Response(status=200)


def main():
    # Trigger any available delivery report callbacks from previous produce() calls
    # see: https://github.com/confluentinc/confluent-kafka-python/issues/16
    producer.poll(0)

    app.run(host='0.0.0.0', port=8401)


if __name__ == '__main__':
    main()
