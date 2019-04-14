import time


def login():
    return"login:这是一个动态网页，时间是：%s"% time.ctime()

def register():
    return"register这是一个动态网页，时间是：%s"% time.ctime()

def profile():
    return"profile这是一个动态网页，时间是：%s"% time.ctime()

def application(name):
    if name=="/login.py":
    	return login()
    elif name=="/register.py":
    	return register()
    elif name=="/profile.py":
    	return profile()
    else:
        return "-----not found-----"
