def set_func1(func):
	print("正在装饰1")
	def call_func1(*args,**kwargs):
		print("验证1")
		return func(*args,**kwargs)
	return call_func1

def set_func2(func):
	print("正在装饰2")
	def call_func2(*args,**kwargs):
		print("验证2")
		return func(*args,**kwargs)
	return call_func2

@set_func1
@set_func2
def test1(num,*args,**kwargs):
	print("----test1----%d"% num)
	
ret1=test1(100)
print(ret1)

