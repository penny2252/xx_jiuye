import socket
import re
import time

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
    client_socket_list=list()
    while True:
        #time.sleep(0.5)
        try:
            #print('当前链接数量：%s'% len(client_socket_list))
            #等待接入
            new_socket,client_addr=tcp_server_socket.accept()
            #接收
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for new_socket in client_socket_list:
            try:
                request=new_socket.recv(1024).decode('utf-8')
            except Exception as ret:
                pass
            else:
                if request:
                    try:
                        service_client(new_socket,request)
                    except Exception as ret:
                        pass
                else:
                    new_socket.close()
                    client_socket_list.remove(new_socket)
        #发送
    tcp_server_socket.close()

if __name__=='__main__':
    main()
