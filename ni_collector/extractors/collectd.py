# -*- coding: utf-8 -*-
#
# custom measurement metric name for each collectd plugin
# the name of the function should match the corresponding plugin name
#

from __future__ import division
import sys, traceback, logging
from ni_collector.config import cfg

logger = logging.getLogger(__name__)

def get_measurements(data):
    result = []
    try:
        for i in range(0, len(data['values'])):
            measurement = "%s___%s___%s___%s" %(
                data['host'],
                get_metric_name(data),
                data['dsnames'][i],
                data['dstypes'][i],
                )
            epoch_ms = data['time'] * 1000
            result.append((measurement, float(data['values'][i]), epoch_ms))
    except Exception as e:
        logger.warning(e, exc_info=True)
    return result

def get_metric_name(data):
    # get the corresponding function for the plugin
    func_metric_name = globals().get(data['plugin'])
    if func_metric_name is not None:
        metric_name = func_metric_name(data)
        if metric_name is not None:
            return metric_name

    default_metric_name = "%s___%s___%s___%s" %(
            data['plugin'],
            data['plugin_instance'],
            data['type'],
            data['type_instance'],
        )
    return default_metric_name


def memory(data):
    if data['type'] == 'memory' and data['type_instance'] == 'free':
        return 'memory_free'

def cpu(data):
    if data['type'] == 'percent' and data['type_instance'] == 'active':
        return 'cpu_usage'

def interface(data):
    if data['type'] in ['if_octets', 'if_packets', 'if_dropped']:
        return ('%s___%s' %(data['plugin_instance'], data['type']))

def virt(data):
    if data['type'] == 'memory' and data['type_instance'] == 'unused':
        return 'memory_free'

    if data['type'] == 'virt_vcpu':
        # we need to convert cpu time (ns) into percentage.
        # We enable storeRate in collectd so the value is gauge
        # We do not need to consider interval since storeRate already handle it
        # 10000000: 10^9 / 100
        data['dstypes'][0] = 'gauge'
        data['values'][0] = (int)(data['values'][0]) / 10000000
        return ('%s___%s' %(data['type_instance'], 'per_pcpu_usage'))

    if data['type'] == 'virt_vcpu_steal':
        data['dstypes'][0] = 'gauge'
        data['values'][0] = (int)(data['values'][0]) / 10000000
        return ('%s___%s' %(data['type_instance'], 'per_pcpu_steal'))

    if data['type'] == 'virt_vcpu_guest_avg':
        data['dstypes'][0] = 'gauge'
        data['values'][0] = (int)(data['values'][0]) / 10000000
        return "cpu_usage"

    if (data['type'] in ['if_octets', 'if_packets', 'if_dropped']):
        return ('%s___%s' %(data['type_instance'], data['type']))

    if (data['type'] in ['disk_ops', 'disk_octets']):
        return ('%s___%s' % (data['type_instance'], data['type']))

def docker(data):
    return "%s___%s___%s" %(
        data['plugin_instance'],
        data['type'],
        data['type_instance'],
    )


def ping(data):
    if data['type'] == 'ping':
        other_host = data['type_instance']
        # other host is IP address format: x.x.x.x. Re-format to NI-Compute-x-x
        other_host = other_host.split('.')
        other_host = "%s-%s-%s" %("NI-Compute", other_host[2], other_host[3])

        return ('%s___%s' %(other_host, data['type']))


def ipmi(data):
    # https://stackoverflow.com/questions/20461847/str-startswith-with-a-list-of-strings-to-test-for
    if data['type_instance'].startswith(("Pwr Consumption", "System Level")):
        return "power_consumption"