import random,re,copy
brand = {'a':'方块','b':'梅花','c':'红桃','d':'黑桃'}
# brand = {'a':'方块'}
brand_code = ['a','b','c','d']

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
    

def biggerthan(mypokers,thepokers):
    return


def checktype(thepokers):
    check = copy.deepcopy(thepokers)
    diccheck = {}
    # i = 0
    for x in check:

        num = finddigi(x)
        if num in diccheck.keys():
            diccheck[num] +=1
        else:
            diccheck[num] = 1
        # i +=1
        # print(i)
    calls = set([v for k,v in diccheck.items()])
    # print('the:',calls
    # print (check,diccheck)

    if calls == {1}:
        if len(check) == 1:
            return('单')
        else:
            return('顺子')
    elif calls == {2} and 'bj0' not in check:
        if len(check) == 2:
            return('对子')
        else:
            return('连对')
    elif calls == {2} and 'bj0' in check:
        return('王炸')
    elif calls == {3}:
        if len(calls) == 3:
            return('三张')
        else:
            return('连三')
    elif calls == {3,1}:
        if len(check) == 4:
            return('三带一')
        else:
            return('飞机3-1')
    elif calls == {3,2}:
        if len(check) == 5:
            return('三带二')
        else:
            return('飞机3-2')
    elif calls == {3,2,1}:
            return('飞机3-1')
    elif calls == {4,2} or calls == {4,1}:
        if len(check) == 6:
            return('四带一')
        # elif calls == {4,2}:
        #     print('可能是飞机4-2',calls)
        else:
            return('四带二')
    else:
        return('不清楚')
        # for x in calls:
        #     print('set',x)


class CanSend(list):

    def twaax(self,num):
        '''Triplet with an attached x triplet with a pair added, the ranking being determined by the rank of the triplet - for example Q-Q-Q-x(maybe 1 or 1-1) beats 10-10-10-x.'''
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
        '''Sequence of triplets with attached cards- an extra card is added to each triplet. Only the triplets have to be in sequence, for example 
7-7-7-8-8-8-3-6. The attached cards must be different from all the triplets and from each other. Although triplets of 2 cannot be included in the triplets sequence, a 2 or a joker or one of each can be attached, but not both jokers. '''
        tri = self.sox(3)
        # print('飞机',tri)
        thecards = [] 
        for xarr in tri:
            thecard = [xarr]
            others = aftersend(self,xarr)
            a = CanSend(others)
            sigs = a.thesames(num)

            # print('飞机-1:',xarr,sigs)
            for s in sigs:
                newcard = copy.copy(xarr)
                if s in xarr:
                    continue
                thecards.append(newcard+s)
        return thecards


    def sox(self,num=2):
        '''Sequence of pairs or triplet'''
        # flagnum = 6 if num
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
            # print('-----sop:',same,theone,cans)

        # print('最后:',len(same),len(self.thesames(2)))
        if len(same)==len(self.thesames(num))*num>=6:
            cans.append(same)
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


def checkcansend(checklist,typename):
    b = CanSend(checklist)
    if typename == '单':
        return b.thesames(1)
    elif typename == '对子':
        return b.thesames(2)
    elif typename == '三张':
        return b.thesames(3)
    elif typename == '炸弹':
        return b.thesames(4)
    elif typename == '王炸':
        return b.wangzha()
    elif typename == '顺子':
        return b.shunza()
    elif typename == '三带一':
        return b.twaax(1)
    elif typename == '三带二':
        return b.twaax(2)
    elif typename == '连对':
        return b.box(2)
    elif typename == '连三':
        return b.box(3)
    elif typename == '飞机3-1':
        return b.sotwax(1)
    elif typename == '飞机3-2':
        return b.sotwax(2)
    elif typename == '四带一':
        return b.qs(1)
    elif typename == '四带二':
        return b.qs(2)


def main():
    pokers = getTotalPokers()
    a = deal(pokers)[0]
    # newa = rewash(a)
    newa =  ['d6', 'c7', 'a9', 'b9', 'a10', 'b10', 'c10', 'a11', 'b11', 'c11', 'd11', 'a12', 'b12', 'c12', 'a13', 'b1', 'sj0']
    # newa = ['d3', 'b4', 'a5', 'c6', 'a7', 'b7', 'a8', 'a9', 'a10', 'd10', 'a11', 'b11', 'd11', 'a12', 'b12', 'c12', 'd1']
    # newa = ['a5', 'b5', 'c6', 'a7', 'a9', 'a10', 'b10', 'b11', 'c11', 'b12', 'c12', 'd12', 'c13', 'd13', 'a1', 'b1', 'c1']
    # newa = ['b3', 'a4', 'c4', 'c7', 'b9', 'd9', 'a10', 'b10', 'b11', 'c11', 'c13', 'd13', 'a1', 'b1', 'a2', 'b2', 'c2']
    print('手牌：',newa)
    # checkleft(newa)


    test = [  'a12', 'b12',  'c12', 'd12',  'c13', 'd13']
    # test = ['bj0','sj0']
    typename = checktype(test)
    cansend = checkcansend(newa,typename)
    print(typename,cansend)



if __name__ == '__main__':
    main()



'''
    def single(self):
        copyv = copy.copy(self)
        single = [copyv.pop(0)]
        cans = [single]
        while len(copyv) > 0:
            theone = copyv.pop(0)
            if  (finddigi(theone)== finddigi(single[-1])):
                pass
            else:
                single = [theone]
                cans.append(single)

        return cans
def doubles(self):
        copyv = copy.copy(self)
        cans = []
        while len(copyv) > 0:
            digital0 = re.findall("\d+", copyv[0])[0]
            for i in range(1,len(copyv)):
                digitali = re.findall("\d+", copyv[i])[0]
                if digitali == digital0:
                    cans.append([copyv[0],copyv[i]])
            copyv.pop(0)
        return cans

    def triple(self):
        copyv = copy.copy(self)
        cans = []
        while len(copyv) > 0:
            # print('hah')
            
            digital0 = re.findall("\d+", copyv[0])[0]
            flag = copyv.pop(0)
            same = [flag]

            for x in copyv:
                digital= re.findall("\d+", x)[0]
                if digital == digital0 and len(same)<3:
                    same.append(x)
                elif len(same)>=3:
                    continue
            if len(same) == 3:
                print(3)
                cans.append(same)
            elif len(same) == 4:
                times4 = copy.copy(same)
                for x in times4:

                    cans.append([y for y in times4 if y!=x])

            [copyv.remove(k) for k in same if k in copyv]

        return cans

    def quad(self):
        copyv = copy.copy(self)
        cans = []
        while len(copyv) > 0:
            
            digital0 = re.findall("\d+", copyv[0])[0]
            flag = copyv.pop(0)
            same = [flag]


            # digital = re.findall("\d+", copy[0])[0]
            for x in copyv:
                digital= re.findall("\d+", x)[0]
                if digital == digital0:
                    same.append(x)

            if len(same)>3:
                cans.append(same)

            [copyv.remove(k) for k in same if k in copyv]

        return cans


    def twaap(self):
        #Triplet with an attached pair- a triplet with a pair added, the ranking being determined by the rank of the triplet - for example Q-Q-Q-6-6 beats 10-10-10-K-K.
        tri = self.thesames(3)
        thecards = [] 
        for xarr in tri:
            thecard = [xarr]
            others = send(self,xarr)
            a = CanSend(others)
            sigs = a.thesames(2)

            # print('3-2:',xarr,sigs)
            for s in sigs:
                newcard = copy.copy(xarr)
                if s in xarr:
                    continue
                thecards.append(newcard+s)
        return thecards




    def twaac(self):
    #Triplet with an attached card,so for example 9-9-9-3
        tri = self.thesames(3)
        thecards = [] 
        for xarr in tri:
            thecard = [xarr]
            others = send(self,xarr)
            a = CanSend(others)
            sigs = a.thesames(1)
            for s in sigs:
                newcard = copy.copy(xarr)
                if s in xarr:
                    continue
                thecards.append(newcard+s)
        return thecards

'''

    