from threading import Thread
from time import sleep
g_num=0

def test1(num):
    global g_num
    for i in range(num):
        g_num+=1
    print('test1:%s'% str(g_num))

def test2(num):
    global g_num
    for i in range(num):
        g_num+=1
    print('test2:%s'% str(g_num))

def main():
    #target指定线程去那个函数指定代码，args调用函数过程中传递什么数据过去
    t1=Thread(target=test1,args=(1000000,))
    t2=Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    #等待上面的执行完毕
    sleep(5)
    print('main:%s'% g_num)


if __name__ == '__main__':

    main()
