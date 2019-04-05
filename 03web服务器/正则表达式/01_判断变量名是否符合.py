import re

def main():
    names=['age','_age','1age','age1','a_age','age_1_','age!','a#123']
    for name in names:
        ret=re.match(r'^[a-zA-Z_]\w*$',name)
        if ret:
            print('符合：',name)
        else:
            print('不符合：',name)





if __name__=='__main__':
    main()
