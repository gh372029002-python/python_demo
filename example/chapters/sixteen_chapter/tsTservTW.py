#!/usr/bin python
#-*-coding:utf-8-*-
#使用 Twisted Internet 类的时间戳 TCP 服务器

from    twisted.internet    import  protocol, reactor
from    time    import  ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    """docstring for TSServProtocol"""
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print   '...connected from:', clnt
        pass

    def dataReceived(self,data):
        self.transport.write('[%s] %s'  % (ctime(),data))
        pass

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'        
reactor.listenTCP(PORT,factory)
reactor.run()