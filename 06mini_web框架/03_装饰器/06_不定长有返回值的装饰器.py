def set_func(func):
	def call_func(*args,**kwargs):
		print("验证1")
		return func(*args,**kwargs)
	return call_func
@set_func 
def test1(num,*args,**kwargs):
	print("----test1----%d"% num)
	print("----test1----",args)
	print("----test1----",kwargs)
	return "ok"
ret1=test1(100)
ret2=test1(100,200)
print(ret1)
print(ret2)

@set_func
def test2(num):
	pass
ret3=test2(100)
print(ret3)