import gevent,time
from gevent import monkey

#使用下面语句实现非gevent方式的延时，不需要改变原有代码
monkey.patch_all()

def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #利用monkey可以使用time等方式延时，而不需要转换gevent延时
        time.sleep(0.5)
#print('1')
#g1=gevent.spawn(f,5)
#print('2')
#g2=gevent.spawn(f,5)
#print('3')
#g3=gevent.spawn(f,5)
#g1.join()
#g2.join()
#g3.join()
#可以使用另外一种方式建立一个gevent列表添加任务
gevent.joinall([
        gevent.spawn(f,5),
        gevent.spawn(f,5),
        gevent.spawn(f,5)
])
