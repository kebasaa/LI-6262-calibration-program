# http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
# contains a suggestion to modify to show only available COM ports in Linux. May need to use it

import logging
log = logging.getLogger('root')

import serial

# For serial_ports
import serial.tools.list_ports

import re

# Returns a dictionnary containing both the device name and description (makes it easier to identify by the user)
def serial_ports():
    result = {}
    result["device"] = []
    result["name"] = []
    for p in serial.tools.list_ports.comports():
        result["device"].append(p.device)
        result["name"].append(re.sub("(.*?) \((.*?)\)", "\g<1>", p.description)) # removes the repetition of the name
    x = 0
    for port in result["device"]:
        log.info(str("Found " + result["device"][x] + " " + result["name"][x]))
        x += 1
    return(result)