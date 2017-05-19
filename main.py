#!/usr/bin/env python

'''
 Max Kessler <max.e.kessler@gmail.com>
 
 Main routine for the fauxmo WeMo emulator based on
 http://www.makermusings.com/2015/07/13/amazon-echo-and-home-automation/
'''

import sys
import time
import logging
import fauxmo
import handler

#~ logging.basicConfig(filename='wemo.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)

# List of scripts to run on the Raspberri pi.
# Each entry is a list with the following elements:
#
# name of the virtual switch
# object with 'on' and 'off' methods
# port # (optional; may be omitted)

# NOTE: As of 2015-08-17, the Echo appears to have a hard-coded limit of
# 16 switches it can control. Only the first 16 elements of the FAUXMOS
# list will be used.

SCRIPTS = [
	['test', handler.script_handler("test_script_on.sh", "test_script_off.sh")]
]

# Set up our singleton for polling the sockets for data ready
p = fauxmo.poller()

# Set up our singleton listener for UPnP broadcasts
u = fauxmo.upnp_broadcast_responder()
u.init_socket()

# Add the UPnP broadcast listener to the poller so we can respond
# when a broadcast is received.
p.add(u)

# Create our FauxMo virtual switch devices
for one_faux in SCRIPTS:
	if len(one_faux) == 2:
		# a fixed port wasn't specified, use a dynamic one
		one_faux.append(0)
	switch = fauxmo.fauxmo(one_faux[0], u, p, None, one_faux[2], action_handler = one_faux[1])

logging.debug("Entering main loop\n")

while True:
	try:
		# Allow time for a ctrl-c to stop the process
		#~ logging.debug("targets in the poller: {}".format(p.targets))
		p.poll(100)
		time.sleep(0.1)
		#~ logging.debug("after first sleep.")
		#~ print("hello!")
		#~ time.sleep(1)
	except Exception as e:
		logging.critical(e)
		break
