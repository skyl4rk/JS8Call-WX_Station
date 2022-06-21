# JS8Call-WX_Station

Upon request, report weather station data over JS8Call.

## Prerequisites

This script is to be installed at a weather station with JS8Call

The script will be run at the same time JS8Call is running.

### Dependencies
* python-requests
* js8call

## Usage

From a remote location, an amateur radio operator may request a weather report from the weather station by sending a directed message:

(Weather Station Callsign) (Trigger Text?)

### Example

F1ZXO REPORT?

F1ZXO should respond by sending a weather report as a message to the inbox of the requesting station.

This script is yet untested, please confirm that it will run before installation.
