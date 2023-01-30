#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: David Manouchehri <manouchehri@protonmail.com>
# This script will always echo back data on the UDP port of your choice.
# Useful if you want nmap to report a UDP port as "open" instead of "open|filtered" on a standard scan.
# Works with both Python 2 & 3.

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 8125

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

payload = ''
while True:
	payload_byte, client_address = sock.recvfrom(1024)
	payload += payload_byte.decode('utf-8')
	# print("Echoing data back to " + str(client_address))
	print(payload)
	# sent = sock.sendto(payload, client_address)
