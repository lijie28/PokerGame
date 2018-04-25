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


    def joinin(self,client,name):
        # self.menbers.append([client,name])
        # # print '目前成员',self.menbers
        # 
        self.menbers.join(client,name)
        if len(self.menbers) == 3:
            return True
        return False
            

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




def setName(newgame,dicmessage,client,server):
    if len(newgame.menbers)<3:
            # ip = client['address'][0]
            name = dicmessage['data']
            print '加入了：',client,name
            isfull = newgame.joinin(client,name)

            #告诉全世界有新成员加入
            newmenbers = [x[1] for x in newgame.menbers]
            dicdata = {'action':'newMenber',
            'data':newmenbers
            }
            senddata = json.dumps(dicdata)
            for x in newgame.menbers:
                server.send_message(x[0],senddata)

            if isfull:
                print '满人：',newgame.menbers,'发牌'
                newgame.dipper()
                print '发牌情况：',newgame.pokers,'地主牌是：',newgame.landlord[1]

                for i,x in enumerate(newgame.menbers):
                    yourpokers = json.dumps(
                        {'action':'receivePokers',
                        'data':newgame.pokers[i][1][0]
                    })
                    server.send_message(x[0],yourpokers)

                askstr = json.dumps(
                        {'action':'askLandlord',
                        'data':newgame.landlord[1]
                        })
                server.send_message(newgame.menbers[0][0],askstr)

    else:
        print '满人了'


def setLandlord(newgame,dicmessage,client,server):
    print '抢地主'
    if dicmessage['data'] == True:
        for i,x in enumerate(newgame.menbers):
            if x[0] == client:
                newgame.confirmLandlord(x[1])
                for n,p in newgame.pokers:
                    if n == x[1]:
                        strpokers = json.dumps({
                            'action':'receivePokers',
                            'data':p[0]
                            })
                        server.send_message(client,strpokers)


                strtellnext = json.dumps({
                    'action':'askToSend',
                    'data':newgame.owner[1]
                    })
                server.send_message(client,strtellnext)#服务器告诉下一个出牌
    else:

        for i,x in enumerate(newgame.menbers):
            if x[0] == client:
                if i == len(newgame.menbers)-1:
                    print '重新开始'
                else:

                    askstr = json.dumps(
                            {'action':'askLandlord',
                            'data':newgame.landlord[1]
                            })
                    server.send_message(newgame.menbers[i+1][0],askstr)

                    print '问下一个',newgame.menbers[i+1][0]
                break


def sendPokers(newgame,dicmessage,client,server):
    lps=dicmessage['data']
    condiction = poker.send(newgame.checkHandpokers(),lps,newgame.owner[1])
    # newgame.owner[0]

    if condiction and len(lps)==0:
        print 'pass了：',lps
        # newgame.owner 
        nextone = newgame.tellnext()
        if newgame.owner[0] == nextone:
            newgame.owner[1]=None

        strmes = json.dumps({
            'action':'sendSuccess',
            'data':lps
            })
        server.send_message(client,strmes)#告知出牌成功



        server.send_message(client,strmes)

        strtellnext = json.dumps({
            'action':'askToSend',
            'data':newgame.owner[1]
            })
        nextclient = None
        for c,n in newgame.menbers:
            if n == newgame.sender:
                nextclient = c
        server.send_message(nextclient,strtellnext)#服务器告诉下一个出牌



        #告知全世界谁出了啥牌
        name = None
        leftCount = None
        for c,n in newgame.menbers:
            if c == client:
                name = n
                
        for n,p in newgame.pokers:
            if n == name:
                leftCount = len(p[0])

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


        strmes = json.dumps({
            'action':'sendSuccess',
            'data':lps
            })
        server.send_message(client,strmes)#告知出牌成功

        strtellnext = json.dumps({
            'action':'askToSend',
            'data':newgame.owner[1]
            })
        nextclient = None
        for c,n in newgame.menbers:
            if n == newgame.sender:
                nextclient = c
        server.send_message(nextclient,strtellnext)#服务器告诉下一个出牌


        #告知全世界谁出了啥牌
        name = None
        leftCount = None
        for c,n in newgame.menbers:
            if c == client:
                name = n
                
        for n,p in newgame.pokers:
            if n == name:
                leftCount = len(p[0])

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
        strmes = json.dumps({
            'action':'sendFail',
            'data':lps
            })
        server.send_message(client,strmes)#告知出牌失败
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



    # def main():
    # #先凑够3人
    # newgame = GameProcess()
    # while len(newgame.menbers)<3:
    #     name = ask('等待加入')
    #     if name and name != '':
    #         newgame.joinin('',name)
    # print '满人：',newgame.menbers,'发牌'
    # newgame.Dipper()

    # print '发牌情况：',newgame.pokers,'地主牌是：',newgame.landlord[1]

    # for m in newgame.menbers:
    #     ans = ask('%s 地主牌是：%s,抢地主吗？'%(m,newgame.landlord[1]))
    #     if ans == '抢':
    #         newgame.confirmLandlord(m[1])
    #         break

    # if not newgame.landlord[0]:
    #     print '没人抢地主，重新发牌'
    #     main()

    # print newgame.pokers

    # while len(newgame.pokers[0][1][0])>0 and len(newgame.pokers[1][1][0])>0 and len(newgame.pokers[2][1][0])>0:
    #     ans = None
    #     if newgame.owner[1]:
    #         ans = ask('【%s】你的手牌：%s 请出大于%s的牌'%(newgame.sender,newgame.checkHandpokers()[0],newgame.owner[1]))
    #     else:
    #         ans = ask('【%s】你的手牌：%s 请出牌'%(newgame.sender,newgame.checkHandpokers()[0]))
        
    #     if ans =='q' or ans =='quit':
    #         break
    #     ans = ans.replace("'",'').replace(" ",'')
    #     lps = ans.split(',')

    #     print newgame.checkHandpokers(),lps

    #     condiction = poker.send(newgame.checkHandpokers(),lps,newgame.owner[1])
    #     if condiction and len(lps)==0:
    #         print 'pass了：',ans,lps
    #         # newgame.owner 
    #         nextone = newgame.tellnext()
    #         if newgame.owner[0] == nextone:
    #             newgame.owner[1]=None

    #     elif condiction:
    #         print ans,lps

    #         newgame.owner[0]= newgame.sender
    #         newgame.owner[1]= lps
    #         newgame.tellnext()
    #     else:
    #         print 'error，请重新出牌',lps

    # # print '剩余手牌：\n',newgame.pokers[0][1][0],'\n',newgame.pokers[1][1][0],'\n',newgame.pokers[2][1][0]
    # for i in range(3):
    #     strf = ''
    #     if len(newgame.pokers[i][1][0]) ==0 :
    #         strf = '胜者'
    #     print strf,newgame.menbers[i] ,'剩余手牌：',newgame.pokers[i][1][0]