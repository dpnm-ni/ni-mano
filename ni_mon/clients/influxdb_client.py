# -*- coding: utf-8 -*-
from ni_mon.config import cfg
from ni_mon.models.monitoring_entry import MonitoringEntry

from datetime import date, datetime
from influxdb import InfluxDBClient

from flask import current_app


client = InfluxDBClient(host=cfg['influxdb_client']['server'],
                        database=cfg['influxdb_client']['database'])

def get_between_timestamps(host, measurement_type, start_time: int, end_time: int):
    measurement = u"%s___%s" %(host, measurement_type)
    mon_entries = []

    query = "SELECT time,value FROM \"{measurement}\" WHERE time >= $start_time_ns AND time <= $end_time_ns;".format(
                measurement=measurement,
                )
    bind_params = {
                    'start_time_ns': start_time * 10**9,
                    'end_time_ns': end_time * 10**9,
                }
    result = client.query(query=query, bind_params=bind_params, epoch='ms')
    points = list(result.get_points(measurement=measurement))

    for point in points:
        time_datetime = datetime.fromtimestamp(point['time']/(10**3))
        mon_entry = MonitoringEntry(
                timestamp=time_datetime,
                component_type=None,
                component_id=host,
                measurement_type=measurement_type,
                measurement_value=float(point['value'])
            )

        mon_entries.append(mon_entry)

    return mon_entries

def get_measurement_types(id):

    measurement_types = []

    # TODO: check id param to prevent sql injection
    query = " SHOW MEASUREMENTS WITH MEASUREMENT =~ /^{}___.*/".format(id)
    result = client.query(query=query)

    points = list(result.get_points())

    if len(points) >= 0:
        for point in points:
            measurement_types.append(point['name'].replace("{}___".format(id), ''))

    return measurement_types
