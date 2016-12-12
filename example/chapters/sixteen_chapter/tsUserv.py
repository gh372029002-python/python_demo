#/usr/bin python
#-*-coding:utf-8-*-
#UDP通信实例

from    socket  import  *
from    time    import  ctime


def main():
    print '__main__'
    HOST    =   ''
    PROT    =   21567
    BUFSIZ  =   1024
    ADDR    =   (HOST,PROT)

    udpSerSock  =   socket(AF_INET,SOCK_DGRAM)
    udpSerSock.bind(ADDR)

    while True:
        print 'waiting for message...'
        data,addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto('[%s] %s' % (ctime(),data),addr)
        print '...received from and returned to:', addr
        pass
    udpSerSock.close()
if __name__ == '__main__':
    main()