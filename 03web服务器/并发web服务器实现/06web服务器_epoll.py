import socket
import re
import select

def service_client(new_socket,request):
    #接受http请求GET / HTTP/1.1
    #request=new_socket.recv(1024).decode('utf-8')
    re_list=request.splitlines()[0]
    name='.'
    name+=re.match(r'[^/]+(/[^ ]*)',re_list).group(1)
    if name=='./':
        name='index.html'
    print(request)
    #返回http数据
    f=open(name,'rb')
    body=f.read()
    f.close()
    response_body=body

    response_header='HTTP/1.1 200 OK\r\n'
    response_header+='Content-Length:%d\r\n'% len(response_body)
    response_header+='\r\n'
    
    response=response_header.encode('utf-8')+response_body
    new_socket.send(response)
    #new_socket.close()
def main():
    #创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #绑定服务器信息
    tcp_server_socket.bind(('',7890))
    #监听
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)#设置套接字为非堵塞
    #创建一个epoll对象
    epl=select.epoll()
    #将监听套接字注册到epoll中，检测是否有输入
    epl.register(tcp_server_socket.fileno(),select.EPOLLIN)
    fd_event_dict=dict()
    while True:
        fd_event_list=epl.poll()#默认会堵塞，直到os检测到数据到来，通过事件通知方式告诉这个程序此时才会有解堵塞,返回一个列表，[(fd,event)],第一部分文件描述，第二部分是事件
        for fd,event in fd_event_list:
            if fd==tcp_server_socket.fileno():
                #等待接入
                new_socket,client_addr=tcp_server_socket.accept()
                epl.register(new_socket.fileno(),select.EPOLLIN)
                fd_event_dict[new_socket.fileno()]=new_socket
            elif event==select.EPOLLIN:
                recv_data=fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    try:
                        service_client(fd_event_dict[fd],recv_data)
                    except Exception as ret:
                        pass
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
        #发送
    tcp_server_socket.close()

if __name__=='__main__':
    main()
