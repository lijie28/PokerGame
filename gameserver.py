# -*- coding: utf-8 -*-
import poker,json
from newser import NewServer


        
class GameMenber(list):
    def checkIp(self,client):
        ip = client['address'][0]
        for c,n in self:
            if ip == c['address'][0]:
                c = client
                return n
        return ''


    def tellName(self,client):
        for c,n in self:
            if c == client:
                return n


    def tellClient(self,name):
        for c,n in self:
            if n == name:
                return c


    def join(self,client,name):
        self.append([client,name])

    def isfull(self):
        if len(self) >= 3:
            return True
        return False


    def __init__(self):
        self = []



class Game():
    # def send
    def tellnext(self):
        for i,x in enumerate(self.menbers):
            if x[1] == self.sender :
                if i == len(self.menbers)-1:
                    self.sender = self.menbers[0][1]
                    break
                else:
                    self.sender = self.menbers[i+1][1]
                    break
        return self.sender

    def tellPokers(self,name):
        for n,p in self.pokers:
            if n == name:
                return p[0]

    def checkHandpokers(self):
        name = self.sender
        for p in self.pokers:
            if p[0] == name:
                return p[1]


    def confirmLandlord(self,name):
        for p in self.pokers:
            if p[0] == name:
                p[1][0] = poker.rewash(p[1][0]+self.landlord[1])
                self.landlord[0] = p[0]
                self.sender = p[0]
                self.owner = [p[0],None]
                break
            

    def dipper(self):
        pokers = poker.getTotalPokers()
        sortpokers = poker.deal(pokers)
        self.pokers = [[m[1],[poker.rewash(sortpokers[i]),[]]] for i,m in enumerate(self.menbers)]
        self.landlord = [None,sortpokers[3]]


    def __init__(self):
        self.processname = (
            '等待成员加入',
            '抢地主',
            '出牌'
            )
        # gm = GameMenber()
        self.menbers = GameMenber()


def ask(q):
    return raw_input('%s\n:'%q)




def jsondump(jsonname,datavalue,target=''):
    return json.dumps({
            'action': jsonname,
            'data':datavalue
            })

def setName(newgame,dicmessage,client,server):
    if len(newgame.menbers)<3:
            # ip = client['address'][0]
            name = dicmessage['data']
            print '加入了：',client,name

            newgame.menbers.join(client,name)

            #告诉全世界有新成员加入
            newmenbers = [x[1] for x in newgame.menbers]
            for x in newgame.menbers:
                server.send_message(x[0],jsondump('newMenber',newmenbers))

            if newgame.menbers.isfull():

                print '满人：',newgame.menbers,'发牌'
                newgame.dipper()
                print '发牌情况：',newgame.pokers,'地主牌是：',newgame.landlord[1]

                for i,x in enumerate(newgame.menbers):
                    server.send_message(x[0],jsondump('receivePokers',newgame.pokers[i][1][0]))

                server.send_message(newgame.menbers[0][0],jsondump('askLandlord',newgame.landlord[1]))

    else:
        print '满人了'



def setLandlord(newgame,dicmessage,client,server):
    print '抢地主'
    if dicmessage['data'] == True:

        landlord_name = newgame.menbers.tellName(client)
        newgame.confirmLandlord(landlord_name)
        p = newgame.tellPokers(landlord_name)

        #告诉他重新洗牌
        server.send_message(client,jsondump('receivePokers',p))

        #告诉让他出牌
        server.send_message(client,jsondump('askToSend',newgame.owner[1]))
    
    else:

        for i,x in enumerate(newgame.menbers):
            if x[0] == client:
                if i == len(newgame.menbers)-1:
                    print '重新开始'
                else:
                    server.send_message(newgame.menbers[i+1][0],jsondump('askLandlord',newgame.landlord[1]))

                    print '问下一个',newgame.menbers[i+1][0]
                break


def sendPokers(newgame,dicmessage,client,server):
    lps=dicmessage['data']
    condiction = poker.send(newgame.checkHandpokers(),lps,newgame.owner[1])

    if condiction and len(lps)==0:
        print 'pass了：',lps
        # newgame.owner 
        nextone = newgame.tellnext()
        if newgame.owner[0] == nextone:
            newgame.owner[1]=None

        server.send_message(client,jsondump('sendSuccess',lps))#告知出牌成功


        nextclient = None
        for c,n in newgame.menbers:
            if n == newgame.sender:
                nextclient = c
        server.send_message(nextclient,jsondump('askToSend',newgame.owner[1]))#服务器告诉下一个出牌



        #告知全世界谁出了啥牌
        name = newgame.menbers.tellName(client)
        leftCount = len(newgame.tellPokers(name))



        print '我是',name,'还剩',leftCount

        strtoall = json.dumps({
                'action':'othersend',
                'data':{
                    'name':name,
                    'poker':lps,
                    'count':leftCount
                    }
                })


        for c,n in newgame.menbers:
            if n == name:
                continue
            server.send_message(c,strtoall)


    elif condiction:
        print lps

        newgame.owner[0]= newgame.sender
        newgame.owner[1]= lps
        newgame.tellnext()

        server.send_message(client,jsondump('sendSuccess',lps))#告知出牌成功


        nextclient = None
        for c,n in newgame.menbers:
            if n == newgame.sender:
                nextclient = c
        server.send_message(nextclient,jsondump('askToSend',newgame.owner[1]))#服务器告诉下一个出牌


        #告知全世界谁出了啥牌
        name = newgame.menbers.tellName(client)
        leftCount = len(newgame.tellPokers(name))
 
        print '我是',name,'还剩',leftCount

        strtoall = json.dumps({
                'action':'othersend',
                'data':{
                    'name':name,
                    'poker':lps,
                    'count':leftCount
                    }
                })

        for c,n in newgame.menbers:
            if n == name:
                continue
            server.send_message(c,strtoall)

    else:
        server.send_message(client,jsondump('sendFail',lps))#告知出牌失败
        print 'error，请重新出牌',lps




def received(client, server, message):                   
    print("%s Client(%d) said: %s" % (client['address'][0],client['id'], message))  
    dicmessage = json.loads(message) 
    print '成员：',newgame.menbers

    if dicmessage['action'] == 'setName':
        setName(newgame,dicmessage,client,server)

    elif dicmessage['action'] == 'setLandlord':
        setLandlord(newgame,dicmessage,client,server)

    elif dicmessage['action'] == 'sendPokers':
        sendPokers(newgame,dicmessage,client,server)

    else:
        print dicmessage['action'],dicmessage['data']

    
def new_client(client, server):                                                 
    print("New client connected and was given id %d %s" % (client['id'],client['address'][0]))      
    name = newgame.menbers.checkIp(client)  
    if name == '':
        print '暂无此clint',client
    else:
        print '已经加入过了',name


def client_left(client, server):                                                
    print(" %s Client(%d) disconnected" % (client['address'][0],client['id']))   



def main():
    global newgame 
    newgame = Game()
    #先凑够3人
    global server
    server = NewServer(9001,"0.0.0.0",received,new_client,client_left)


if __name__ == '__main__':
    main()


