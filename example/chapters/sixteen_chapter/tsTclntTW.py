#/usr/bin python
#-*-coding:utf-8-*-
#使用 Twisted Internet 类的时间戳 TCP 服务器

from twisted.internet import protocol,reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    """docstring for TSClntProtocol"""
    
    def sendData(self):
        data = raw_input('>')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()
        pass

    def dataReceived(self,data):
        print data
        self.sendData()
        pass


class TSClntFactory(protocol.ClientFactory):
    """docstring for TSClntFatory"""
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory()) 
reactor.run()       