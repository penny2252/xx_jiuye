

def creat_num(num):
    a,b=0,1
    current_num=0
    while current_num<num:
        #如果函数中有yield，就不是一个函数，而是一个生成器模板
        #用for调用生成器yield会暂停，并返回，然后再继续并返回一直到结束
        yield a
        a,b =b,a+b
        current_num+=1
#创建生成器对象        
a=creat_num(10)
print(a)
#for num in a:
#    print(num)
ret=next(a)
print(ret)
ret=next(a)
print(ret)
