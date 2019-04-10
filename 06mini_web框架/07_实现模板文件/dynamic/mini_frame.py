def index():
	with open("./templates/index.html") as f:
		content=f.read()
	return content	
def center():
	with open("./templates/center.html") as f:
		content=f.read()
	return content	


def application(env,start_response):
	start_response("200 OK",[("Content-Type","text/html;charset=utf-8")])
	name=env["PATH_INFO"]
	if name=="/index.py":
		return index()
	elif name=="/center.py":
		return center()
	else:
		return "hello晓晓"
