import gevent,time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #需要有中断、延时实现多协程切换，但是time延时无法使用，需要使用gevent.sleep
        gevent.sleep(0.5)
print('1')
g1=gevent.spawn(f,5)
print('2')
g2=gevent.spawn(f,5)
print('3')
g3=gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()
