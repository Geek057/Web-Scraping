#!/usr/bin/env python3
# encoding: UTF-8
import socket
name = input('enter name of site : ')
ip = socket.gethostbyname(name)
print(ip)