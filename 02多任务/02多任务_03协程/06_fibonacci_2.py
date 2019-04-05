class Fibonacci(object):
    def __init__(self,a,b,num,nums):
        self.a=a
        self.b=b
        self.nums=0
        self.num=num
    def __iter__(self):
        return self    
    def __next__(self):
        if self.nums<self.num:
            ret=self.a
           # self.nums.append(self.a)
            self.a,self.b =self.b,self.a+self.b
            self.nums+=1
            return ret
        else:
            raise StopIteration

nums=list()
fibonacci=Fibonacci(0,1,10,nums)
for i in fibonacci:
    print(i)
