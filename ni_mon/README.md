# NI-Mon
NI-Mon server provides RESTful APIs for other applications (such as NI-AI-module) to query various metrics of Openstack cluster.
NI-Mon is generated with [swagger-codegen](https://github.com/swagger-api/swagger-codegen), using the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
- Python 3.5.2+
- Running Openstack cluster that NI-Mon monitors
- Running kafka instance and kafka_extractor instance
- Packages

    ```
    sudo apt-get install libssl-dev
    ```

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m ni_mon
```

## Configuration
Edit files in `config` folder.

## Documentation
Open in browser for documentation:

```
http://localhost:8383/ui/
```

The API definition lives here:

```
http://localhost:8383/swagger.json
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t ni_mon .

# starting up a container
docker run -p 8383:8383 ni_mon
```
