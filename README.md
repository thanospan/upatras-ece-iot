# UPatras-ECE-IoT

## Requirements

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose V2](https://docs.docker.com/compose/cli-command/#installing-compose-v2) (Already installed with Docker Desktop)

Optional:
* [Python](https://www.python.org/downloads/)
* [paho-mqtt](https://pypi.org/project/paho-mqtt/)
* [Postman](https://www.postman.com/downloads/)

## Usage

```
git clone https://github.com/thanospan/upatras-ece-iot.git
cd upatras-ece-iot
git checkout fall-2021
docker compose --env-file ./config/env/.env up
```
```
Node-RED: http://localhost:1880
Orion Context Broker: http://localhost:1026/v2
MongoDB: localhost:27017
Mosquitto MQTT Broker: localhost:1883
```
When referenced from another Docker container in the same network, localhost has to be replaced with the container_name assigned in docker-compose.yml.

E.g., in order to connect to the Mosquitto MQTT Broker using Node-RED, localhost:1883 has to be replaced with mosquitto:1883.
