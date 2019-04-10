def index():
	return "主页"
def login():
	return "登录页面"


def application(env,start_response):
	start_response("200 OK",[("Content-Type","text/html;charset=utf-8")])
	name=env["PATH_INFO"]
	if name=="/index.py":
		return index()
	elif name=="/login.py":
		return login()
	else:
		return "hello晓晓"
