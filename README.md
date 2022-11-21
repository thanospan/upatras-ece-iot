# UPatras-ECE-IoT

## Requirements
- [Docker](https://docs.docker.com/get-docker/)

## Usage
```
git clone https://github.com/thanospan/upatras-ece-iot.git
cd upatras-ece-iot
git checkout fall-2022
docker compose up
```

```
Node-RED: http://localhost:1880
Orion Context Broker: http://localhost:1026/v2
MongoDB: localhost:27017
Mosquitto MQTT Broker: localhost:1883
```

## Setup
- Visit http://localhost:1880
- Press `alt+shift+p`, switch to the `Install` tab and install the `node-red-contrib-web-worldmap` module.
- Copy the Node-RED flows provided in the `node-red` directory.
- Press `ctrl+i` and paste the JSON in order to import the flows.
