def test1(k,b):
	def creat_y(x):
		print(k*x+b)
	return creat_y
test1_1=test1(1,2)
test1_1(0)
test1_1(1)
test1_1(2)
test2=test1(11,22)
test2(0)
test2(1)
test2(2)