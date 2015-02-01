#!/usr/bin/python
'''
Created on Jan 4, 2015

@author: Dennis
'''

import socket

#target_host = "www.google.com"
target_host = raw_input("Enter a ULR to query: ").lower()
target_port = 80
send_data = "GET / HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n"
print send_data

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(send_data)
#client.send("GET / HTTP/1.1\r\nHost: target_host \r\n\r\n")

# receive some data
response = client.recv(4096)

print response
