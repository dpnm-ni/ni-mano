# -*- coding: utf-8 -*-

import yaml
import os

package_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(package_dir,"config/config.yaml")

with open(config_file_path, 'r') as yml_config_file:
    cfg = yaml.load(yml_config_file, yaml.SafeLoader)
