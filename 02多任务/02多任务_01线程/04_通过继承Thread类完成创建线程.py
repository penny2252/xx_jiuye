import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            msg = "i'm"+self.name+'@'+str(i)
            print(msg)
        

 
if __name__ == "__main__":
    t=MyThread()
    t.start()
