import threading
from time import sleep,ctime


def sing():
    """唱歌 5秒钟"""
    for i in range(5):

        sleep(1)
        print("11111%s"%ctime())


def dance():
    """跳舞"""        
    for i in range(5):
        sleep(1)
        print("跳舞111%s"%ctime())


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        sleep(1)
        print(threading.enumerate(),ctime()) 
        if len(threading.enumerate())<=1:
            break

 
if __name__ == "__main__":
    main()
