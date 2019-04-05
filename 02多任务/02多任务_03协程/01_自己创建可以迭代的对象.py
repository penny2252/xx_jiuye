from collections import Iterable
from collections import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    # 如果没有__iter__方法这个类建立的对象无法迭代,通过下方print语句可以验证i
    def __iter__(self):
        # 如果想要一个对象成为一个可以迭代的对象，必须要用这个方法
        print('111')
        return ClassIterator()


class ClassIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        return 11


classmate = Classmate()

classmate.add("老王")
classmate.add("王二")
classmate.add("张三")
# print('判断classmate是否是个可以迭代的对象：', isinstance(classmate, Iterable))
# classmate_iterator =iter(classmate)
# print('判断classmate_iterator是否是一个迭代器：', isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))
# 在可以迭代的前提下，iter函数可以得到对象的——iter——方法的返回值
# ——iter——方法的返回值是一个迭代器
for name in classmate:
    print(name)
    time.sleep(1)


"""
for temp in xxx_obj:
    pass
以上迭代实现的3个条件
1、判断xxx_obj是否可迭代，相当于‘isinstance(xxx_obj,Iterable)’
2、在第1不成立的前提下，调用iter函数得到xxx_obj对象的__iter__方法的返回值
3、__iter__方法的返回值是一个迭代器



"""
