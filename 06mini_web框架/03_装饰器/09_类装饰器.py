class set_func1(object):
	def __init__(self,func):
		self.func=func
	def __call__(self,*args,**kwargs):
		return "<td>"+self.func()+"</td>"


@set_func1 #test1=set_func1(test1)
def test1():
	return "xiaoxiao"
	

print(test1())

