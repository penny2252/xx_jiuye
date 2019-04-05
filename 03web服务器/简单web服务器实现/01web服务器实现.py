import socket


def service_client(new_socket):
    #接受http请求GET / HTTP/1.1
    request=new_socket.recv(1024)
    
    print(request)
    #返回http数据
    response='HTTP/1.1 200 OK\r\n'
    response+='\r\n'
    body='<h1>hello</h1>'
    response+=body
    new_socket.send(response.encode('utf-8'))
    new_socket.close()
def main():
    #创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定服务器信息
    tcp_server_socket.bind(('',7890))
    #监听
    tcp_server_socket.listen(128)
    while True:
        #等待接入
        new_socket,client_addr=tcp_server_socket.accept()
        #接收
        service_client(new_socket)
        #发送
    tcp_server_socket.close()

if __name__=='__main__':
    main()
