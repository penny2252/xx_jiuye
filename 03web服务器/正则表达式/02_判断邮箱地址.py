import re

def main():
    email=input('请输入邮箱地址')
    ret=re.match(r'^[a-zA-Z0-9_]{4,20}@163\.com$',email)
    if ret:
        print('符合%s'% ret.group())
    else:
        print('不符合%s'% email)




if __name__=='__main__':
    main()
