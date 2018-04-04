nums = [12,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

bushu = 0

def count():
    global bushu 
    bushu += 1
    print('步')


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



class exlist(list):
    def exchange(self,a,b):
        self[a],self[b]=self[b],self[a]


def myQuickSort(num,l,r):
    count()
fakequickSort(nums)
print(nums,bushu)





def atosort(nums,after):

    right = []
    newnums = exlist(nums)
    for i,x in enumerate(newnums):

        if i ==0:
            continue

        if len(right) == 0:
            if x<newnums[0]:
                pass
            else:
                right.append(i)
                # print('无',i,right)
        else:
            if x<newnums[0]:
                k = right.pop(0)
                right.append(i)
                # print('交换',i,k)
                newnums.exchange(i,k)
                # print('结果',newnums)
                
            else:
                right.append(i)

    theone = None
    if len(right) == len(newnums) - 1:
        theone = 0
        # print('确定了在最前：',newnums[0])

    elif len(right) == 0 :
        newnums.exchange(0,len(newnums)-1)
        theone = len(newnums) - 1
        # print('确定了在最后：',newnums[0])
                # print('有',i,right)
    else:
        count = len(newnums) - len(right) 
        newnums.exchange(0,count-1)
        theone = count -1
        # if x<nums[0] and len(right) == 0:
        #     pass
        #     # print('左',y,leftl)
        # else:
            # print('右',y,rightl)

    print(nums,'\n',newnums,'\ntheone:',theone,' ',newnums[theone],after)
    if theone!=0:
        # pass
        atosort(newnums[:theone],newnums[theone+1:len(newnums)])
        # atosort(newnums[theone+1:len(newnums)])
    # return newnums,right


# print(nums[1:len(nums)])
# atosort(nums,[])
# newl,right = atosort(nums)
# print(nums,'\n',newl,'\nright:',right,len(right),len(newl))

# a = exlist(nums)
# print(a)
# # a=a
# a.exchange(1,2)
# print (a)

# print(nums)
# # a = nums[2]
# # nums[2] = nums[3]  
# # nums[3] = a
# exchange(nums[2],nums[3])
# # nums[2],nums[3]=nums[3],nums[2]
# print(nums)

