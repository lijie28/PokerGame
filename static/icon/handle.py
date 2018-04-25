import os



brand_code = ['c','d','b','a']

for i,file in enumerate(os.listdir('.')):
    print i,file
    p = (i)/13
    q = (i)%13
    if 'png_' in file:
        # print p,q
        newname = None
        if p<4:
            if q==0:
                newname = brand_code[p]+'13'+'.png'
            else:
                newname = brand_code[p]+str(q)+'.png'

            print p,q,newname
            os.rename(file,newname)