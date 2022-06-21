import sys
import time
import json
from js8net import *
import re
import requests
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-r", "--remote", action="store", dest="ADDR", type="string",
                  help="set a remote host address")
parser.set_defaults(ADDR="localhost")
parser.add_option("-p", "--port",
                  action="store", dest="PORT", default=True, type="int",
                  help="set JS8 port (default 2442)")
parser.set_defaults(PORT=2442)
parser.add_option("-t", "--trigger", action="store", dest="trig", type="string",
                  help="set the trigger expression (default REPORT?)")
parser.set_defaults(trig='REPORT?')

(options, args) = parser.parse_args()

js8host=options.ADDR
js8port=options.PORT

print("Connecting to JS8Call...")
start_net(js8host,js8port)
print("Connected.")
get_band_activity()
my_call = get_callsign()
print(my_call + ' WX Station Active...')
print()

trigger = options.trig

last=time.time()
while(True):
    time.sleep(0.1)
    if(not(rx_queue.empty())):
        with rx_lock:
            rx=rx_queue.get()
            f=open("rx.json","a")
            f.write(json.dumps(rx))
            f.write("\n")
            f.close()
# Check for a message directed to my callsign    
            if(rx['type']=="RX.DIRECTED" and my_call == rx['params']['TO']):
                directed_message_to_my_call = rx['params']['TEXT']
# Split the recieved directed message
                split_message = re.split('\s', directed_message_to_my_call)
# Search for trigger
                item_count = len(split_message)
                for i in range(item_count):
#                    print(split_message[i])
#                    try:
                    if split_message[i] == trigger:
                        message = open('/opt/js8call-wx_station/wx_report.txt')
                        send_inbox_message(message)
                        
