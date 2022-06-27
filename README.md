# JS8Call-WX_Station

Upon request, report weather station data over JS8Call.

## Prerequisites

This script is to be installed at a weather station with JS8Call

The script will be run at the same time JS8Call is running.

### Dependencies
* python-requests library
* js8call

## Installation with systemd service
To get the systemd feature, it is recommended to clone the repo in `/opt/` and link the service file to systemd:
```sh
cd /opt/
git clone https://github.com/f4iey/JS8Call-WX_Station.git
ln -s /opt/JS8Call-WX_Station/wx_station.service /etc/systemd/system
```
After that, it is possible to enable and start as an usual service after starting JS8CALL:
```sh
systemctl enable wx_station
systemctl start wx_station
```

## Usage

### From the station

After starting JS8Call, the program can be started with the service or standalone with the `python` command.
By default, the host is set on localhost and JS8CALL default port. These parameters can be changed using `--remote` and `--port` options.
e.g, for a remote instance of JS8CALL (on hamnet):
```sh
python wx_station-0.1.py -r f4kkx.ampr.org -p 6942
```
It is also possible to change the wake word with the `--trigger` option
```sh
python wx_station-0.1.py -r f4kkx.ampr.org -t WX?
```

### From a remote location

An amateur radio operator may request a weather report from the JS8CALL station by sending a directed message with the format:

`[CALLSIGN] [WAKE WORD]`

### Example

`F1ZXO REPORT?`

F1ZXO should respond by sending a weather report as a message to the inbox of the requesting station.

This script is yet untested, please confirm that it will run before installation.
