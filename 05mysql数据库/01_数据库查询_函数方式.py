from pymysql import *


def goods_name():
    conn=connect(host='localhost',port=3306,user='root',password='mysql',database='jingdong',charset='utf8')
    cursor=conn.cursor()
    count=cursor.execute('select * from goods')
    for i in range(count):
        result=cursor.fetchone()
        print(result)
    cursor.close()
    conn.close()


def goods_cates_name():
    conn=connect(host='localhost',port=3306,user='root',password='mysql',database='jingdong',charset='utf8')
    cursor=conn.cursor()
    count=cursor.execute('select * from goods_cates')
    for i in range(count):
        result=cursor.fetchone()
        print(result)
    cursor.close()
    conn.close()

def goods_brands_name():
    conn=connect(host='localhost',port=3306,user='root',password='mysql',database='jingdong',charset='utf8')
    cursor=conn.cursor()
    count=cursor.execute('select * from goods_brands')
    for i in range(count):
        result=cursor.fetchone()
        print(result)
    cursor.close()
    conn.close()



def main():
    while True:
        a=input('请输入操作(1、所有产品；2、所有分类；3、所有厂家；4、退出):')
        if a =='1':
            goods_name()
        elif a=='2':
            goods_cates_name()
        elif a=='3':
            goods_brands_name()
        elif a=='4':
            break
        else:
            print('输入错误请重新输入')


if __name__=='__main__':
    main()
