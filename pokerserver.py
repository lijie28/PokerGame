#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket
import time  
import json

class UdpServer(object):
    def search(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # PORT = 10086
        sock.bind(('', 10086))

        mes = json.dumps({'action': 'searchForConection','value': 'testhaha' })
        sendDataLen = sock.sendto(mes,("255.255.255.255", 10086))

        print sendDataLen

        # print 'Listening for xbroadcast at ', s.getsockname()
        # while True:
        #   data, address = s.recvfrom(1024)
          # print 'Server received from {}:{}'.format(address, data.decode('utf-8'))


    def tcpServer(self):
        print 'enter serve'
        count = 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 10086))       # 绑定同一个域名下的所有机器
        
        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)


            if data['action'] == 'searchForConection':
                # mes = "收到 %d" % count
                name = socket.getfqdn(socket.gethostname()) 
                mes = json.dumps({'action': 'receive','value': name })
                
                sendDataLen = sock.sendto(mes,(remoteHost, remotePort))
                print mes
            
        sock.close()
            
if __name__ == "__main__":

    if len(sys.argv)<2:
        udpServer = UdpServer()
        udpServer.tcpServer()
    else:
        udpServer = UdpServer()
        udpServer.search()
