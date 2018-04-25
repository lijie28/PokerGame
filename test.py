# -*- coding: utf-8 -*-

# !/usr/bin/env python 
# coding: utf-8 
import threading 
import time 





import time
bushu = 0

def count():
    global bushu 
    bushu += 1
    # print('步')

def fakein_quickSort(num,l,r):
    count()
    if l>=r:#如果只有一个数字时，结束递归
        return
    flag=l
    for i in range(l+1,r+1):#默认以第一个数字作为基准数，从第二个数开始比较，生成索引时要注意右部的值
        if num[flag]>num[i]:
            tmp=num[i]
            del num[i]
            num.insert(flag,tmp)
            flag+=1
    fakein_quickSort(num,l,flag-1)#将基准数前后部分分别递归排序
    fakein_quickSort(num,flag+1,r)

def fakequickSort(num):
    fakein_quickSort(num,0,len(num)-1)


def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        v[low] = key
    return low
def quicksort(v, left, right):
    count()
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v

# s = [12,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
# a = time.time()
# print("before sort:",a)
# # quicksort(s, left = 0, right = len(s) - 1)
# # fakequickSort(s)
# sorted(s)   
# b = time.time()
# print("after sort:",b,bushu,'用时：',b-a,'\n',s)



class Person(object):

    def tellteacher(self,func):
        print "teacher,my name is %s,i'm %s years old." %(self.name,self.age)

        func(self.repo)

    """docstring for Person"""
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.sex = age

        if int(self.age)<18:
            self.repo = '未成年'
        else:
            self.repo = '成年'

        

class GPerson(Person):
    """docstring for GPerson"""
    # def __init__(self, arg):
    #     super(GPerson, self).__init__()
    #     self.arg = arg
        
        

def registered(name,age,sex):
    print '注册'+name + age


def report(detail):
    print '报告结果:',detail


p = Person('jack','12')
# p.tellteacher(report)

def observe(obj,proname,func):
    class 
    
    print obj.__getattribute__(proname)
    obj.__setattr__(proname,18)
    print obj.__getattribute__(proname)
    # print obj.__format__(proname)


# print
observe(p,'age',report)







