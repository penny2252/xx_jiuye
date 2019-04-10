import socket
import re
import multiprocessing
import time
import mini_frame


class WSGIServer(object):
    def __init__(self):
        #创建套接字
        self.tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        #绑定服务器信息
        self.tcp_server_socket.bind(('',7890))
        #监听
        self.tcp_server_socket.listen(128)


    def service_client(self,new_socket):
        #接受http请求GET / HTTP/1.1
        request=new_socket.recv(1024).decode('utf-8')
        re_list=request.splitlines()[0]
        name=''
        name+=re.match(r'[^/]+(/[^ ]*)',re_list).group(1)
        if name=='/':
            name='/index.html'
        print(request)
        #返回http数据
        #如果返回请求资源不是以.py结尾，那么就认为是静态资源
        if not name.endswith(".py"):
            response='HTTP/1.1 200 OK\r\n'
            response+='\r\n'
            try:
                f=open("./html"+name,'rb')
            except:
                response="HTTP/1.1 404 NOT FOUND\r\n"
                response+="\r\n"
                response+="-------file not found-------"
                new_socket.send(response.encode("utf-8"))
            else:
                body=f.read()
                f.close()
                new_socket.send(response.encode('utf-8'))
                new_socket.send(body)
        else:            
            env=dict()
            body=mini_frame.application(env,self.set_response_header)
            response="HTTP/1.1 %s\r\n"% self.status
            for temp in self.header:
                response+="%s:%s\r\n"% (temp[0],temp[1])
            response+="\r\n"
            response+=body
            new_socket.send(response.encode("utf-8"))
        new_socket.close()
    def set_response_header(self,status,header):
        self.status=status
        #服务器的信息在服务器里添加
        self.header=[("server","mini_web v1.0")]
        #框架的信息在框架引用后返回添加
        self.header+=header
        
    def run_forever(self):
        while True:
            #等待接入
            new_socket,client_addr=self.tcp_server_socket.accept()
            #接收
            try:
                p=multiprocessing.Process(target=self.service_client,args=(new_socket,))
                p.start()
                new_socket.close()
            except:
                FileNotFoundError
            #发送
        self.tcp_server_socket.close()

def main():
    wsgi_server=WSGIServer()
    wsgi_server.run_forever()

if __name__=='__main__':
    main()
