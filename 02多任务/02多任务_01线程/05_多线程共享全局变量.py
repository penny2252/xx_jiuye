from threading import Thread
from time import sleep
g_num=100

def test1():
    global g_num
    g_num+=1
    print('test1:%d'% g_num)

def test2():
    
    print('test2:%d'% g_num)

def main():
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    t1.start()
    sleep(0.5)
    t2.start()
    sleep(1)
    print('main:%d'% g_num)


if __name__ == '__main__':

    main()
