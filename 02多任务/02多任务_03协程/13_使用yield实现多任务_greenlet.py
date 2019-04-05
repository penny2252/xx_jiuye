import time
from greenlet import greenlet

def task_1():
    while True:
        print('.....1.....')
        gr2.switch()
        time.sleep(1)
        
def task_2():
    while True:
        print('.....2.....')
        gr1.switch()
        time.sleep(1)
        

gr1=greenlet(task_1)
gr2=greenlet(task_2)
gr1.switch()
