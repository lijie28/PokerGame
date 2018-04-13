# -*- coding: utf-8 -*-
import poker


class GameProcess():

    def confirmLandlord(name):
        return 


    def joinin(self,ip):
        self.menbers.append(ip)


    def Dipper(self):
        pokers = poker.getTotalPokers()
        sortpokers = poker.deal(pokers)
        self.pokers = [(m,sortpokers[i]) for i,m in enumerate(self.menbers)]
        self.landlordcards = sortpokers[3]

        # return self.pokers
        # self.pokers = []
        # for i,p in enumerate(sortpokers):
        #     self.pokers.append(self.menbers[i],p)


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

    print '发牌情况：',newgame.pokers

    # for m in newgame.menbers:
    #     ans = ask('%s 地主牌是：%s,抢地主吗？',m,sortpokers[3])
    #     if ans == '抢':
    #         newgame.confirmLandlord(m)










if __name__ == '__main__':
    main()