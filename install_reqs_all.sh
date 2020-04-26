#!/bin/bash
#
# install requirements for dev.
#

pip install -r ni_mon/requirements.txt
pip install -r ni_nfvo/requirements.txt
pip install -r kafka_extractor/requirements.txt
./install_reqs_tests.sh
