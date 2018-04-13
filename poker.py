# -*- coding: utf-8 -*-
import random,re,copy

from itertools import combinations




brand = {'a':'方块','b':'梅花','c':'红桃','d':'黑桃'}
# brand = {'a':'方块'}
brand_code = ['a','b','c','d']



class MyPokers(object):
    def send(self,pokers):
        for p in pokers:
            if p not in self.handpokers:
                return False

        for p in pokers:
            self.sendpokers.append(p)
            self.handpokers.remove(p)


        return True


    def __init__(self,handpokers):
        self.handpokers = handpokers
        self.sendpokers = []





def getpoke():
    dic = {}
    i = 1
    for a in range(3,14):
        for b in brand_code:
            dic[b+str(a)] = i
            i+=1
    for a in range(1,3):
        for b in brand_code:
            dic[b+str(a)] = i
            i+=1
    dic['sj0'] = i
    i+=1
    dic['bj0'] = i   
    return dic


# def setpoke(poke):



def getTotalPokers(hasJoker = True):
    totalp = [k+str(x) for x in range(1,14) for k,v in brand.items()]
    if hasJoker:
        # pass
        totalp.append('bj0')#bj代表大王 ,sj代表小王
        totalp.append('sj0')
    return totalp


def randompick(pokers,num):
    thepicks = random.sample(pokers, num)  #从list中随机获取5个元素，作为一个片断返回  
    for tp in thepicks:
        # if tp in pokers:
        pokers.remove(tp)
    return thepicks,pokers

def rewash(pokers):
    dic = getpoke()
    # for i,x in enumerate(pokers):
    #     pokers[i] = dic[x]
    npokers = [dic[x] for x in pokers]
        # print(pokers[i],dic[x])
    # newpokers = sorted(npokers)

    newpokers = [k for x in sorted(npokers) for k,v in dic.items() if x == v]


    # sorted(pokers, key=lambda student: student.age)
    return newpokers

def finddigi(str):
    return int(re.findall("\d+", str)[0])

def aftersend(pokers,sends):
    mypokers = copy.copy(pokers)
    mysends = copy.copy(sends)
    # [k for x in mypokers for k in mysends ]
    for x in mysends:
        if x in mypokers:
            mypokers.remove(x)
    # for s in mypokers:
    #     if s in mysends:
    #         mypokers.remove(s)
    return mypokers
    

# def biggerthan(mypokers,thepokers):
#     return

def countpokers(thepokers):
    check = copy.deepcopy(thepokers)
    diccheck = {}
    # i = 0
    for x in check:

        num = finddigi(x)
        if num in diccheck.keys():
            diccheck[num] +=1
        else:
            diccheck[num] = 1
    return diccheck




            # cans.append(back)


def checkmax(thepokers):
    def biggerthan(x1,x2):
        a = range(3,14)
        b = [1,2]
        
        if x1 in a and x2 in a and x1>x2:
            return True
        elif x1 in b and x2 in b and x1>x2:
            return True
        elif x1 in b and x2 in a:
            return True
        elif x1 == 0 or x2== 0 :
            return None
        return False

    themax = [0,0]
    for k,v in diccheck.items():
        # print(k,v)
        if v > themax[1]:
            themax[1] = v
            themax[0] = k
        elif v == themax[1]:
            if biggerthan(k,themax[0]):
                themax[0] = k

def checktype(thepokers):
    def biggerthan(x1,x2):
        a = range(3,14)
        b = [1,2]
        
        if x1 in a and x2 in a and x1>x2:
            return True
        elif x1 in b and x2 in b and x1>x2:
            return True
        elif x1 in b and x2 in a:
            return True
        elif x1 == 0 or x2== 0 :
            return None
        return False

    diccheck = countpokers(thepokers)
    calls = set([v for k,v in diccheck.items()])

    

    themax = [0,0]
    for k,v in diccheck.items():
        # print(k,v)
        if v > themax[1]:
            themax[1] = v
            themax[0] = k
        elif v == themax[1]:
            if biggerthan(k,themax[0]):
                themax[0] = k

    if calls == {1}:
        if len(thepokers) == 1:
            return('单',themax[0],len(thepokers))
        else:
            return('顺子',themax[0],len(thepokers))
    elif calls == {2} and 'bj0' not in thepokers:
        if len(thepokers) == 2:
            return('对子',themax[0],len(thepokers))
        else:
            return('连对',themax[0],len(thepokers))
    elif calls == {2} and 'bj0' in thepokers:
        return('王炸',themax[0],len(thepokers))
    elif calls == {3}:
        if len(calls) == 3:
            return('三张',themax[0],len(thepokers))
        else:
            return('连三',themax[0],len(thepokers))
    elif calls == {3,1}:
        if len(thepokers) == 4:
            return('三带一',themax[0],len(thepokers))
        else:
            return('飞机3-1',themax[0],len(thepokers))
    elif calls == {3,2}:
        if len(thepokers) == 5:
            return('三带二',themax[0],len(thepokers))
        elif len(thepokers) == 8 or len(thepokers) == 16:
            return('飞机3-1',themax[0],len(thepokers))
        else:
            return('飞机3-2',themax[0],len(thepokers))
    elif calls == {3,2,1}:
            return('飞机3-1',themax[0],len(thepokers))
    elif calls == {4,2} or calls == {4,1}:
        if len(thepokers) == 6:
            return('四带一',themax[0],len(thepokers))
        else:
            return('四带二',themax[0],len(thepokers))
    else:
        return('不清楚')
        # for x in calls:
        #     print('set',x)


class CanSend(list):
    def checkcansend(self,typename):
        # b = CanSend(checklist)
        if typename == '单':
            return self.thesames(1)
        elif typename == '对子':
            return self.thesames(2)
        elif typename == '三张':
            return self.thesames(3)
        elif typename == '炸弹':
            return self.thesames(4)
        elif typename == '王炸':
            return self.wangzha()
        elif typename == '顺子':
            return self.shunza()
        elif typename == '三带一':
            return self.twaax(1)
        elif typename == '三带二':
            return self.twaax(2)
        elif typename == '连对':
            return self.box(2)
        elif typename == '连三':
            return self.box(3)
        elif typename == '飞机3-1':
            return self.sotwax(1)
        elif typename == '飞机3-2':
            return self.sotwax(2)
        elif typename == '四带一':
            return self.qs(1)
        elif typename == '四带二':
            return self.qs(2)


    def bt(self,arr):
        strtype,themax,thelen = checktype(arr)
        print('bt',strtype,themax,thelen)

        cans = self.checkcansend(strtype)
        bigger = []

        for x in cans:
            if checktype(x)[1]>themax and checktype(x)[2] == thelen:
                # print('大于的：',x)
                bigger.append(x)

        if len(self.wangzha())>0:
            # print('大于的：',self.wangzha())
            bigger = bigger + self.wangzha()

        if len(self.thesames(4))>0:
            # print('大于的：',self.thesames(4))
            bigger = bigger + self.thesames(4)

        return bigger
            # pass
        # print('bt',cans,strtype,themax)

    def twaax(self,num):
        '''Triplet with an attached x triplet with a pair added, the ranking being determined by the r ank of the triplet - for example Q-Q-Q-x(maybe 1 or 1-1) beats 10-10-10-x.'''
        tri = self.thesames(3)
        thecards = [] 
        for xarr in tri:
            thecard = [xarr]
            others = aftersend(self,xarr)
            a = CanSend(others)
            sigs = a.thesames(num)

            # print('3-2:',xarr,sigs)
            for s in sigs:
                newcard = copy.copy(xarr)
                if s in xarr:
                    continue
                thecards.append(newcard+s)
        return thecards

    def qs(self,num=1):
        tri = self.thesames(4)
        # print('飞机',tri)
        thecards = [] 
        for xarr in tri:
            thecard = [xarr]
            others = aftersend(self,xarr)
            a = CanSend(others)
            sigs = a.thesames(num)
            

            while len(sigs)>0:
                theone = sigs.pop(0)
                for x in sigs:
                    thecards.append(xarr+theone+x)
            # for i in range(len(sigs)-1):
            #     newcard = copy.copy(xarr)
            #     s1 = sigs[i]
            #     s2 = sigs[i+1]
            #     thecards.append(newcard+s1+s2)
        return thecards

    #Quadplex set
    def sotwax(self,num=1):
                
        '''飞机3带n
        Sequence of triplets with attached cards- an extra card is added to each triplet. Only the triplets have to be in sequence, for example 
7-7-7-8-8-8-3-6. The attached cards must be different from all the triplets and from each other. Although triplets of 2 cannot be included in the triplets sequence, a 2 or a joker or one of each can be attached, but not both jokers. '''
        tri = self.sox(3)
        thecards = [] 
        
        print('同连三：',len(tri),tri)

        for xarr in tri: 
            print('飞机连三',len(xarr),xarr)
            # if len(xarr)!=k:
            #     continue

            k = int(len(xarr)/3)
            # # thecard = [xarr]

            others = aftersend(self,xarr)
            a = CanSend(others)

            sigs = a.thesames(num)


            if len(sigs)<k:
                continue

            for c in combinations(copy.copy(sigs), k):
                newc = []
                for x in c:
                    newc = newc + x

                hassame = False
                newxarr = [finddigi(x) for x in xarr]
                for s in newc:
                    if finddigi(s) in newxarr:
                        hassame = True
                if hassame:
                    continue

                # print(newc)
                thecards.append(xarr+newc)

        return thecards


    def sox(self,num=2):
        '''Sequence of pairs or triplet'''
        # flagnum = 6 if num
        def segmentation(cans,pokers,num):
            for x in pokers:
                if len(x)>6:
                    front = copy.copy(x)
                    back = copy.copy(x)
                    for i in range(num):
                        front.pop(0)
                        back.pop(-1)
                    # print('new',front,back)
                    segmentation(cans,[front,back],num)
                    if front not in cans:
                        cans.append(front)                
                    if back not in cans:
                        cans.append(back)

        pai = copy.copy(self.thesames(num))
        cans = []
        if len(pai) == 0:
            return cans
        same = pai.pop(0)
        while len(pai)>0:
            theone = pai.pop(0)
            # print('sop----:',same,theone)
            if  (finddigi(theone[0])== finddigi(same[-1])+1 and finddigi(same[-1])!=1) or (finddigi(same[-1])==13 and finddigi(theone[0])==1 ):
                # print('same',same,theone,same+theone)
                same = same + theone

            elif finddigi(theone[0])== finddigi(same[-1]):
                # print('continue')
                continue
            else:
                # print('--结束:',len(same),num*2)
                if len(same)>=6: #连三 是3x2,连对是2x3 结果都是6
                    cans.append(same)
                same = theone

        # print('最后:',len(same),len(self.thesames(2)))
        if len(same)==len(self.thesames(num))*num>=6:
            cans.append(same)

        # result = copy.copy(cans)
        segmentation(cans,cans,num)

        return cans


    def wangzha(self):
        copyv = copy.copy(self)
        cans = []
        same = []
        while len(copyv) > 0:
            theone = copyv.pop(0)
            if theone == 'bj0' or theone == 'sj0':
                same.append(theone)
        if len(same) == 2:
            cans.append(same)
        return cans

    def thesames(self,num):
        copyv = copy.copy(self)
        cans = []
        same = [copyv.pop(0)]
        while len(copyv) > 0:

            theone = copyv.pop(0)
            if finddigi(theone)== finddigi(same[-1]) and len(same)<num:
                same.append(theone)
                if len(copyv) == 0 and len(same) >= num:
                    cans.append(same)
            elif len(same)==num and (finddigi(theone) == finddigi(same[-1])):
                continue
            else:
                if len(same)>=num:
                    cans.append(same)
                same = [theone]

        if len(same)==num:
            cans.append(same)


        return cans

    def shunza(self,num=5):
        copyv = copy.copy(self)
        cans = []
        same = [copyv.pop(0)]
        while len(copyv)>0:
            theone = copyv.pop(0)
            if  (finddigi(theone)== finddigi(same[-1])+1 and finddigi(same[-1])!=1) or (finddigi(same[-1])==13 and finddigi(theone)==1):
                same.append(theone)
                if len(copyv) == 0 and len(same) >= num:
                    cans.append(same)
            elif finddigi(theone)== finddigi(same[-1]):
                continue
            else:
                if len(same)>=num:
                    cans.append(same)
                same = [theone]
        return cans
 


def deal(pokers,gamerole=1):#1是斗地主,2是锄大地
    if gamerole==1:
        # pass
        menberA,pokers = randompick(pokers,17)
        menberB,pokers = randompick(pokers,17)
        menberC,pokers = randompick(pokers,17)
        landlord = pokers
        # print('成员A:',menberA,'\n','成员B:',menberB,'\n','成员C:',menberC,'\n','地主牌:',landlord)
        return menberA,menberB,menberC,landlord


def checkleft(thelefts):
    b = CanSend(thelefts)
    print('\n单出：',b.thesames(1),'\n对子：',b.thesames(2),'\n三张牌：',b.thesames(3),'\n炸弹：',b.thesames(4),'\n王炸：',b.wangzha(),'\n顺子：',b.shunza(),'\n三带一：',b.twaax(1),'\n三带二：',b.twaax(2),'\n连对：',b.sox(2),'\n连三：',b.sox(3),'\n飞机3-1:',b.sotwax(1),'\n飞机3-2：',b.sotwax(2),'\n飞机4-2:',b.qs())





def main():
    pokers = getTotalPokers()
    a = deal(pokers)[0]
    newa = rewash(a)
    newa =  ['a8', 'b8','c8', 'a9', 'b9', 'c9','a10', 'b10', 'c10', 'a11', 'b11', 'c11', 'd11', 'a12', 'b12', 'c12', 'sj0']
    # newa = ['d3', 'b4', 'a5', 'c6', 'a7', 'b7', 'a8', 'a9', 'a10', 'd10', 'a11', 'b11', 'd11', 'a12', 'b12', 'c12', 'd1']
    # newa = ['a5', 'b5', 'c6', 'a7', 'a9', 'a10', 'a11', 'b11', 'c11', 'b12', 'c12', 'd12', 'c13', 'd13', 'a1', 'b1', 'c1']
    # newa = ['b3', 'a4', 'c4', 'c7', 'b9', 'd9', 'a10', 'b10', 'b11', 'c11', 'c13', 'd13', 'a1', 'b1', 'a2', 'b2', 'c2']
    print('手牌：',newa)
    # checkleft(newa)


    # test = ['a2','bj0', 'a9','b9' ,'c9', 'b10',  'c10' ,  'd10']

    test1 = ['a12', 'b12', 'c12', 'sj0']
    test2 = ['a8', 'b8','c8']
    # typename = checktype(test)

    # cansend = checkcansend(newa,typename)
    # print(typename)
    myps = MyPokers(newa)

    print(myps.handpokers,myps.sendpokers)

    if myps.send(test1):
        print('成功出牌',myps.handpokers,myps.sendpokers)
    else:
        print('出牌有问题')

    if myps.send(test2):
        print('成功出牌',myps.handpokers,myps.sendpokers)
    else:
        print('出牌有问题')
        
    # print (countpokers(myps))
    # checkleft(newa)

    # same3 = myps.sotwax(2)

    # bt = myps.bt(test)
    # print('大于的：',bt)

    # for x in same3:
    #     print('有',len(x),'位数',x)
    # print('飞机3：',len(same3),same3)


if __name__ == '__main__':
    main()

