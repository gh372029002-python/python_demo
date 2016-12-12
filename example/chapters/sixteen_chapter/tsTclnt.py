#!/usr/bin python
#-*-coding:utf-8-*-
#TCP 时间戳客户端(tsTclnt.py)

from socket import *

HOST    =   'localhost'
HOST    =   '42.96.141.229'
PORT    =   21567
BUFSIZ  =   1024
ADDR    =   (HOST,PORT)

tcpCliSock  =   socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data    =   raw_input('>')
    if not  data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not  data:
        break
    print data
tcpCliSock.close()