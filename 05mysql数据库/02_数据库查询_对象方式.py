from pymysql import *


class JingDong(object):
    def __init__(self):
        self.conn=connect(host='localhost',port=3306,user='root',password='mysql',database='jingdong',charset='utf8')
        self.cursor=self.conn.cursor()
        
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    @staticmethod
    def print_menu():
        print('------京东-----')
        print('1、查询所有产品')
        print('2、查询产品分类')
        print('3、查询产品品牌')
        print('4、退出')
        return input('请输入操作：')

    def run(self):
        while True:
            a=self.print_menu()
            if a =='1':
                self.goods_name()
            elif a=='2':
                self.goods_cates_name()
            elif a=='3':
                self.goods_brands_name()
            elif a=='4':
                break
            else:
                print('输入错误请重新输入')


    def goods_name(self):
        sql='select * from goods'
        self.execute_sql(sql)

    def goods_cates_name(self):
        sql='select * from goods_cates'
        self.execute_sql(sql)

    def goods_brands_name(self):
        sql='select * from goods_brands'
        self.execute_sql(sql)


def main():
    jd=JingDong()
    jd.run()
   

if __name__=='__main__':
    main()
