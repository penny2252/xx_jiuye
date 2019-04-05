from threading import Thread
from time import sleep
g_num=[100,11]

def test1(temp):
    
    temp.append(33)
    print('test1:%s'% str(temp))

def test2(temp):
    
    print('test2:%s'% str(temp))

def main():
    #target指定线程去那个函数指定代码，args调用函数过程中传递什么数据过去
    t1=Thread(target=test1,args=(g_num,))
    t2=Thread(target=test2,args=(g_num,))
    t1.start()
    sleep(0.5)
    t2.start()
    sleep(1)
    print('main:%s'% g_num)


if __name__ == '__main__':

    main()
