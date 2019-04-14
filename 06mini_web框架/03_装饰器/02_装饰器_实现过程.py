def set_func(func):
	def call_func():
		print("验证1")
		func()
	return call_func
@set_func #test1=set_func(test1)
def test1():
	print("----test1----")
#实现过程
#ret=set_func(test1)
#ret()
#test1=set_func(test1)
test1()
