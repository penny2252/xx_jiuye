def set_func1(func):
	print("正在装饰1")
	def call_func1(*args,**kwargs):
		print("验证1")
		return "<h1>"+func()+"</h1>"
	return call_func1

def set_func2(func):
	print("正在装饰2")
	def call_func2(*args,**kwargs):
		print("验证2")
		return "<td>"+func()+"</td>"
	return call_func2

@set_func1
@set_func2
def test1():
	return "xiaoxiao"
	

print(test1())

