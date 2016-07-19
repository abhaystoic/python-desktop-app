#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
File name : prov.py
Comments : To fetch serial id and certificate from modem. 
Author : Nitin Agarwal <nitin.agarwal@symstream.com>
'''

# export-id (will get modem unique ID)
# export-key (will get modem public key)
# reset-key (will cause modem to remove the private/public key pair)

import socket

host = "10.255.255.245"
port = 50001


def prov_send_command(cmd):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
	return "Failed to connect to target!"
    s.send (cmd)

    data=""
    while True:
        recv = s.recv (1024)
	if len(recv) == 0: break
        data += recv
    s.close();
    return data


def main():
    modem_id = prov_send_command("export-id")
    modem_cert = prov_send_command("export-key")
    modem_details = [modem_id, modem_cert]

    return modem_details