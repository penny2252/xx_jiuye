import multiprocessing


def download_from_web(q):
    #模拟下载数据
    data=[11,22,33,44]
    for temp in data:
        q.put(temp)
    
def analysis_data(q):
    waitting=list()
    while True:
        data=q.get()
        waitting.append(data)
        if q.empty():
            break
    print(waitting)
def main():
    q=multiprocessing.Queue()
    t1=multiprocessing.Process(target=download_from_web,args=(q,))
    t2=multiprocessing.Process(target=analysis_data,args=(q,))
    t1.start()
    t2.start()


    
if  __name__=="__main__":
    main()
