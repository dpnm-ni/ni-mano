# -*- coding: utf-8 -*-
import pdb
from datetime import date, datetime

from confluent_kafka import Consumer, TopicPartition, KafkaError

from ni_mon.models.monitoring_entry import MonitoringEntry
from ni_mon.config import cfg

from flask import current_app


def get_between_timestamps(host, measurement_type, start_time, end_time):
    client = Consumer(cfg['kafka_client']['consumer'])
    topic = u"%s___%s" %(host, measurement_type)

    start_time_ms = start_time * 1000
    end_time_ms = end_time * 1000
    start_tp = TopicPartition(topic, 0, start_time_ms)
    end_tp = TopicPartition(topic, 0, end_time_ms)
    start_offset = client.offsets_for_times([start_tp])[0].offset
    end_offset = client.offsets_for_times([end_tp])[0].offset

    if (start_offset == -1):
        current_app.logger.warning("offset error: start_offset %d. start_time should not be later than now" %(start_offset))
        return None

    if end_offset == -1:
        watermark_offsets = client.get_watermark_offsets(TopicPartition(topic, 0))
        if watermark_offsets is None:
            current_app.logger.error("watermark_offsets is None")
            return None
        end_offset = watermark_offsets[1] - 1

    if (start_offset > end_offset):
        current_app.logger.warning("start_offset %d, end_offset %d. start_time should not be later than end_time" %(start_offset, end_offset))
        return None

    num_mess_to_read = end_offset + 1 - start_offset
    mon_entries = []

    start_tp = TopicPartition(topic, 0, start_offset)
    client.assign([start_tp])
    messages = client.consume(num_mess_to_read)

    for mess in messages:
        if mess.error() is not None:
            current_app.logger.warning(mess.error())
            continue
        time_datetime = datetime.fromtimestamp(mess.timestamp()[1]//1000)
        mon_entry = MonitoringEntry(
            timestamp=time_datetime,
            component_type=None,
            component_id=host,
            measurement_type=measurement_type,
            measurement_value=float(mess.value())
            )

        mon_entries.append(mon_entry)

    client.close()

    return mon_entries
