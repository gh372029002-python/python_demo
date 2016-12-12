#/usr/bin python
#-*-coding:utf-8-*-
#UDP通信实例

from    socket  import  *
from    time    import  ctime


def main():
    HOST = '127.0.0.1'
    PROT = 21567
    BUFSIZ = 1024
    ADDR = (HOST,PROT)
    
    udpCliSock  =   socket(AF_INET,SOCK_DGRAM)

    while True:
        data = raw_input('>')
        if not data:
            break
        udpCliSock.sendto(data,ADDR)
        data,ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print data 
        udpCliSock.close()
        pass  
    udpCliSock.close()


if __name__ == '__main__':
    main()
    pass