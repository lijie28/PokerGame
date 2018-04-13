# -*- encoding:utf-8 -*-
from socket import *
import sys
import threading
import time
#socket - tcp - client.py （客户端）：
reload(sys)
sys.setdefaultencoding("utf8")
 
# 测试，连接本机
HOST = '127.0.0.1'
# 设置侦听端口
PORT = 8555
BUFSIZ = 1024
 
 
class TcpClient:
    ADDR = (HOST, PORT)
 
    def __init__(self):
        self.HOST = HOST
        self.PORT = PORT
        self.BUFSIZ = BUFSIZ
        # 创建socket连接
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        # 起一个线程，监听接收的信息
        self.trecv = threading.Thread(target=self.recvmsg)
        self.trecv.start()
 
    def sendmsg(self,text = None):
        # 循环发送聊天消息，如果socket连接存在则一直循环，发送quit时关闭链接
        # data = text if text else raw_input('>:')
        # self.client.send(data.encode('utf8'))
        # print(u'发送信息到%s：%s' % (self.HOST, data))
        while self.client.connect_ex(self.ADDR):
            
            data = raw_input('>:')
            if not data:
                break
            self.client.send(data.encode('utf8'))
            print(u'发送信息到%s：%s' % (self.HOST, data))
            if data.upper() == "QUIT":
                self.client.close()
                print u"已关闭"
                break
 
    def recvmsg(self):
        # 接收消息，如果链接一直存在，则持续监听接收消息
        try:
            while self.client.connect_ex(self.ADDR):
                data = self.client.recv(self.BUFSIZ)
                print(u'从%s收到信息：%s' % (self.HOST, data.decode('utf8')))
        except Exception, e:
            print str(e)
 
 
if __name__ == '__main__':
    client = TcpClient()
    client.sendmsg('你好吗')