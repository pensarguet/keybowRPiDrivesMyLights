#!/bin/python3
import keybow
import time
import requests
import json
import sys
import logging

log_level_info = {'logging.DEBUG': logging.DEBUG, 
                        'logging.INFO': logging.INFO,
                        'logging.WARNING': logging.WARNING,
                        'logging.ERROR': logging.ERROR,
                        }
config = {}
myButtonState = [0,0,0]

keybow.setup(keybow.MINI)

def setup():
    # Init Keybow light to Green
    keybow.set_pixel(0, 0, 255, 0) # -- Green
    keybow.set_pixel(1, 0, 255, 0) # -- Green
    keybow.set_pixel(2, 0, 255, 0) # -- Green

def activate(URL):
    error = 0
    if URL=="":
        logging.info("URL is empty, nothing to activate")
        return
    else:
        logging.info('Sending request to: ' + URL)

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        error = 1
        logging.error("An Http Error occurred:" + repr(errh))
    except requests.exceptions.ConnectionError as errc:
        error = 1
        logging.error("An Error Connecting to the API occurred:" + repr(errc))
    except requests.exceptions.Timeout as errt:
        error = 1
        logging.error("A Timeout Error occurred:" + repr(errt))
    except requests.exceptions.RequestException as err:
        error = 1
        logging.error("An Unknown Error occurred" + repr(err))
    if error==0:
        logging.info('Response: ' + response.text)
        logging.info('Status code: ' + str(response.status_code))

@keybow.on(index=0)
def handle_key(index, state):
    logging.info("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))
    if state:
        keybow.set_led(index, 255, 0, 0)
    else:
        if myButtonState[index] == 1:
            keybow.set_led(index, 0, 255, 0)
            keybow.show()
            myButtonState[index] = 0
            activate(config["plug0"]["URL-off"])
        else:
            keybow.set_led(index, 255, 0, 0)
            keybow.show()
            myButtonState[index] = 1
            activate(config["plug0"]["URL-on"])

@keybow.on(index=1)
def handle_key(index, state):
    logging.info("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))

    if state:
        keybow.set_led(index, 255, 0, 0)
    else:
        if myButtonState[index] == 1:
            keybow.set_led(index, 0, 255, 0)
            keybow.show()
            myButtonState[index] = 0
            activate(config["plug1"]["URL-off"])
        else:
            keybow.set_led(index, 255, 0, 0)
            keybow.show()
            myButtonState[index] = 1
            activate(config["plug1"]["URL-on"])

@keybow.on(index=2)
def handle_key(index, state):
    logging.info("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))

    if state:
        keybow.set_led(index, 255, 0, 0)
    else:
        if myButtonState[index] == 1:
            keybow.set_led(index, 0, 255, 0)
            keybow.show()
            myButtonState[index] = 0
            activate(config["plug2"]["URL-off"])
        else:
            keybow.set_led(index, 255, 0, 0)
            keybow.show()
            myButtonState[index] = 1
            activate(config["plug2"]["URL-on"])

try:
    with open("./config.json") as f:
        config = json.loads(f.read())
except Exception as e:
    sys.stderr.write("Error: {}".format(e))
    sys.exit(1)

my_log_level_from_config = config['logger']['level']
my_log_level = log_level_info.get(my_log_level_from_config, logging.ERROR)
#logging.basicConfig(filename=config["logger"]["loggingFileName"], encoding='utf-8',format='%(asctime)s, %(levelname)s %(message)s', level=my_log_level )
logging.basicConfig(filename=config["logger"]["loggingFileName"],format='%(levelname)s:%(asctime)s:%(message)s', level=my_log_level)

logging.info("Starting")

setup()
while True:
   keybow.show()
   time.sleep(1.0 / 60.0)
