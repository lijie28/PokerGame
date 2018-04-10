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

s = [12,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
# a = time.time()
# print("before sort:",a)
# # quicksort(s, left = 0, right = len(s) - 1)
# # fakequickSort(s)
# sorted(s)   
# b = time.time()
# print("after sort:",b,bushu,'用时：',b-a,'\n',s)

a = [1, 2, 0, 3, 4, 0, 5, 0, 6]
a = filter(lambda x: x > 0, a)
# for i, x in enumerate(a):
#     print(i,x)



def test():
    av = [1,2,3,4,5]
    bv = [6,7,8,9]
    for a,b in av,bv:
        

        print('在外',a,b)



test()



