#/usr/bin python
#-*-coding:utf-8-*-
#例 16.6 SocketServer 时间戳 TCP 客户端(tsTclntSS.py)

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input(">")
    if not data:
        break
    tcpCliSock.send("%s\r\n" % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print   data.strip()
    tcpCliSock.close()
