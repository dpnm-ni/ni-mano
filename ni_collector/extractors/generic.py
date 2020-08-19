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
    try:
        measurement_name = "%s___%s" % (data['host'], data['measurement_type'])
        return [(measurement_name, float(data['value']), data['epoch_ms'])]
    except Exception as e:
        logger.warning(e, exc_info=True)
