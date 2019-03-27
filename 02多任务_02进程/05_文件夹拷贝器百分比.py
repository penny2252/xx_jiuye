# -*- coding: utf-8 -*-

import multiprocessing
import os,time,random 


def copy(i,source_folder,target_folder,q):

    #t_start=time.time()
    #print('开始拷贝%s'% i )
    source_file=open(source_folder+'/'+i,'rb')
    target_file=open(target_folder+'/'+i,'wb')
    data=source_file.read()
    target_file.write(data)
    source_file.close()
    target_file.close()
    #time.sleep(random.random()*2)
    #t_stop=time.time()
    #print('%s拷贝结束，耗时%0.2f'%(i,t_stop-t_start))
    q.put(i)

def main():
    #获取文件夹名字
    source_folder=input('请输入原文件夹:')
    target_folder=input('请输入目标文件夹:')
    #创建文件夹
    try:
        os.mkdir(target_folder)
    except:
        pass
    #文件名列表
    file_names=os.listdir(source_folder)
    #遍历文件列表，拷贝
    po=multiprocessing.Pool(5)
    q=multiprocessing.Manager().Queue()
    for i in file_names:
        po.apply_async(copy,args=(i,source_folder,target_folder,q))
    po.close()
    a=0
    while True:
        file_name=q.get()
        a+=1
        print('\r拷贝进度：%.2f%%'%(a*100/len(file_names)),end="")
        if a>=len(file_names):
            break
    print()     
    
if __name__=='__main__':
    main()
