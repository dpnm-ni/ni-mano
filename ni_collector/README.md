# Kafka Extractor
Extract raw data sent to kafka (such as data from collectd) and republish them into timeseries-like topics that can be consumed by other applications (such as NI-Mon or NI-AI-module).

## Requirement
Python 2.7

## Usage
Currently, only collectd_extractor is used:
```
python kafka_extractor/collectd_extractor.py
```

## Configuration
The config file also shows which topic available for consume:
```
vi config/config.yaml
```

## Web GUI
We use [kafdrop 3](https://github.com/obsidiandynamics/kafdrop) to monitor available topics and data. This should be automatically installed with Kafka Extractor if using ni-testbed ansible script.
```
http://localhost:9000
```
