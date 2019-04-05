

def creat_num(num):
    print('----1----')
    a,b=0,1
    current_num=0
    while current_num<num:
        #如果函数中有yield，就不是一个函数，而是一个生成器模板
        #用for调用生成器yield会暂停，并返回，然后再次调用生成器后继续执行while循环中yield后续的代码，到yield处后再暂停，并返回，直到再次调用或while循环达到条件结束
        print('----2----')
        yield a
        print('----3----')
        a,b =b,a+b
        current_num+=1
        print('----4----')
    
#创建生成器对象        
#可以创建多个生成器对象，调用时不会冲突
a=creat_num(10)
a2=creat_num(2)
print(a)
ret=next(a)
print('a:',ret)
ret=next(a)
print('a:',ret)
ret=next(a2)
print('a2:',ret)
ret=next(a)
print('a:',ret)
ret=next(a)
print('a:',ret)

