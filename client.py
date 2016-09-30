#!/usr/bin/python
# coding=UTF-8

import socket

IP = "127.0.0.1"
PORT = 49666

while True:
    DATA = raw_input()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(DATA, (IP, PORT))
