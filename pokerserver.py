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
          # udp_gb_client.py
        '''客户端（UDP协议局域网广播）'''


        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        PORT = 10086

        s.bind(('', PORT))
        mes = json.dumps({'action': 'searchForConection','value': 'tests' })
        sendDataLen = s.sendto(mes,('255.255.255.255', PORT))
        # 
        # while True:
        #     print '进来了'
        #     revcData, (remoteHost, remotePort) = s.recvfrom(65535)
        #     print('Listening for broadcast at ', s.getsockname())
        #     mes = json.dumps({'action': 'searchForConection','value': 'tests' })
        #     sendDataLen = s.sendto(mes,(remoteHost, remotePort))
        #     print mes
            # data, address = s.recvfrom(65535)
        #     print('Server received from {}:{}'.format(address, data.decode('utf-8')))


    def tcpServer(self):
        print 'enter serve'
        count = 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 10086))       # 绑定同一个域名下的所有机器
        
        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)

            data = eval(revcData)
            if data['action'] == 'searchForConection':
                # mes = "收到 %d" % count
                name = socket.getfqdn(socket.gethostname()) 
                mes = json.dumps({'action': 'receive','value': name })
                
                sendDataLen = sock.sendto(mes,(remoteHost, remotePort))
                print '接收到：',data
            
        sock.close()
            
if __name__ == "__main__":

    if len(sys.argv)<2:
        udpServer = UdpServer()
        udpServer.tcpServer()
    else:
        udpServer = UdpServer()
        udpServer.search()
