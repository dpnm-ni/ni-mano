# -*- coding: utf-8 -*-

import yaml
import os
import uuid

package_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(package_dir,"config/config.yaml")
with open(file_path, 'r') as yaml_file:
    cfg = yaml.load(yaml_file, yaml.SafeLoader)
    cfg["kafka_client"]["consumer"]["group.id"] = "kafka_extractor_%s" %(uuid.uuid4())

file_path = os.path.join(package_dir,"config/topo.yaml")
with open(file_path, 'r') as yaml_file:
    topo = yaml.load(yaml_file, yaml.SafeLoader)
