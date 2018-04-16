# -*- coding: utf-8 -*-
import poker


class GameProcess():
    def send
    def tellnext(self):
        for i,x in enumerate(self.menbers):
            if x == self.sender :
                if i == len(self.menbers)-1:
                    self.sender = self.menbers[0]
                    break
                else:
                    self.sender = self.menbers[i+1]
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


    def joinin(self,ip):
        self.menbers.append(ip)


    def Dipper(self):
        pokers = poker.getTotalPokers()
        sortpokers = poker.deal(pokers)
        self.pokers = [[m,[poker.rewash(sortpokers[i]),[]]] for i,m in enumerate(self.menbers)]
        self.landlord = [None,sortpokers[3]]


    def __init__(self):
        self.menbers = []


def ask(q):
    return raw_input('%s\n:'%q)



def main():
    #先凑够3人
    newgame = GameProcess()
    while len(newgame.menbers)<3:
        name = ask('等待加入')
        if name and name != '':
            newgame.joinin(name)
    print '满人：',newgame.menbers,'发牌'
    newgame.Dipper()

    print '发牌情况：',newgame.pokers,'地主牌是：',newgame.landlord[1]

    for m in newgame.menbers:
        ans = ask('%s 地主牌是：%s,抢地主吗？'%(m,newgame.landlord[1]))
        if ans == '抢':
            newgame.confirmLandlord(m)
            break

    if not newgame.landlord[0]:
        print '没人抢地主，重新发牌'
        main()

    print newgame.pokers

    while len(newgame.pokers[0][1][0])>0 and len(newgame.pokers[1][1][0])>0 and len(newgame.pokers[2][1][0])>0:
        ans = None
        if newgame.owner[1]:
            ans = ask('【%s】你的手牌：%s 请出大于%s的牌'%(newgame.sender,newgame.checkHandpokers()[0],newgame.owner[1]))
        else:
            ans = ask('【%s】你的手牌：%s 请出牌'%(newgame.sender,newgame.checkHandpokers()[0]))
        
        ans = ans.replace("'",'').replace(" ",'')
        lps = ans.split(',')

        print newgame.checkHandpokers(),lps

        condiction = poker.send(newgame.checkHandpokers(),lps)
        if condiction and len(lps)==0:
            print 'pass了：',ans,lps
            # newgame.owner 
            nextone = newgame.tellnext()
            if newgame.owner[0] == nextone:
                newgame.owner[1]=None

        elif condiction:
            print ans,lps

            newgame.owner[0]= newgame.sender
            newgame.owner[1]= lps
            newgame.tellnext()
        else:
            print 'error，请重新出牌',lps

    print '剩余手牌：\n',newgame.pokers[0][1][0],'\n',ewgame.pokers[1][1][0],'\n',newgame.pokers[2][1][0]









if __name__ == '__main__':
    main()