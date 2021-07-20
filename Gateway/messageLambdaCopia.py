#
# Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

import json
import logging
import platform
import sys
import time

import greengrasssdk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

client = greengrasssdk.client("iot-data")


def message_handler(event, context):
    logger.info("Received message!")
    if "state" in event:
        if event["state"] == "on":
            temp=event["temp"]
            if temp < 10:
                GPIO.output(18,GPIO.LOW)
                client.publish(
                    topic="hello/world/messaggio",
                    queueFullPolicy="AllOrException",
                    payload=json.dumps(
                        {
                            "message": "Va tutto bene. Temperatura rilevata {}".format(temp)
                        }
                    ),
                )
            else:
                GPIO.output(18,GPIO.HIGH)
                client.publish(
                    topic="hello/world/erroreRitorno",
                    queueFullPolicy="AllOrException",
                    payload=json.dumps(
                        {
                            "message": "Messaggio ritorno {}".format(temp)
                        }
                    ),
                )
                client.publish(
                    topic="hello/world/errore",
                    queueFullPolicy="AllOrException",
                    payload=json.dumps(
                        {
                            "message": "NON va bene. TEMPERATURA ELEVATA {}".format(temp)
                        }
                    ),
                )
    