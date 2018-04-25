# -*- encoding:utf-8 -*-
from websocket_server import WebsocketServer                    
import json                
 #// 当新的客户端连接时会提示                                                                        
# Called for every client connecting (after handshake)  
# from gameserver import GameProcess

        
    
def new_client(client, server):                                                 
    print("New client connected and was given id %d %s" % (client['id'],client))        
    # server.send_message_to_all("Hey all, a new c lient has joined us")          

 # // 当旧的客户端离开                                                                         
# Called for every client disconnecting                                         
def client_left(client, server):                                                
    print("Client(%d) disconnected" % client['id'])                         

# // 接收客户端的信息。                                                                             
# Called when a client sends a message                                          
def message_received(client, server, message):                                  
    if len(message) > 200:                                                  
            message = message[:200]+'..'                                    
    # print("%s Client(%d) said: %s" % (client['address'][0],client['id'], message))  
    dicmessage = json.loads(message) 

    # if dicmessage['action'] == 'setName':

    # elif dicmessage['action'] == 'setLandlord':

    # elif dicmessage['action'] == 'sendPoker':

    # else:
    print dicmessage['action'],dicmessage['data']




class NewServer(WebsocketServer):
    """docstring for NewServer"""

    # def startNewGame(self):
    #     newgame = GameProcess()
    #     return newgame

    def send_mes(self,client, message):
        self.send_message(client,message)
        print client, server,message


    def received(self,client, server, message):                   
        print("%s Client(%d) said: %s" % (client['address'][0],client['id'], message))  
        dicmessage = json.loads(message) 
        print '成员：',self.game.menbers

        if dicmessage['action'] == 'setName':
            if len(self.game.menbers)<3:
                # ip = client['address'][0]
                name = dicmessage['data']
                print '加入了：',client,name
                self.game.joinin(client,name)
            else:
                print '满人了'
        else:
            print dicmessage['action'],dicmessage['data']




    def __init__(self,port,address,mr=message_received,nc=new_client,cl=client_left):

        # super(NewServer, self).__init__(port,address) #python3的方法
        WebsocketServer.__init__(self,port,address);#注意此处参数含self 
        # self.arg = arg
        
        # PORT=9001                                                                       
        # self = WebsocketServer(PORT, "0.0.0.0")   
        # self.game = GameProcess()    

        self.set_fn_new_client(nc)                                            
        self.set_fn_client_left(cl)                                          
        self.set_fn_message_received(mr) 

        # print self.client
        # client = {}
        # self.send_message(1,'')
        # self.send_message_to_all()                               
        self.run_forever()
        # self = server




if __name__ == '__main__':
    # main()se
    server = NewServer(9001,"0.0.0.0")
    newgame = server.startNewGame()

    # print server.client      




