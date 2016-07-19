#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" To fetch serial id and certificate from modem. """

__author__ = "Nitin Agarwal"
__copyright__ = "Copyright 2015, Symstream S6 Project"
__maintainer__ = "Nitin Agarwal"
__email__ = "nitin.agarwal@symstream.com"
__status__ = "Development"

# export-id (will get modem unique ID)
# export-key (will get modem public key)
# reset-key (will cause modem to remove the private/public key pair)

import socket
import constants

HOST_MODEM = "10.255.255.245"
PORT_MODEM = 50001

def prov_send_command(cmd):
    "To connect with socket on modem"
    s_connection = socket.socket()
    try:
        #s_connection.settimeout(10) #Aded by Abhay, to include timeout
        s_connection.connect((HOST_MODEM, PORT_MODEM))
    except:
        return constants.FAILURE_MSG_FROM_FETCH
    s_connection.send(cmd)
    data = ""
    while True:
        recv = s_connection.recv(1024)
        if len(recv) == 0:
            break
        data += recv
    s_connection.close()
    return data

def main():
    "To get serial number and certificate of connected modem"
    modem_id = prov_send_command("export-id")
    modem_cert = prov_send_command("export-key")
    modem_details = [modem_id, modem_cert]
    return modem_details
