import socket


def main():

    #创建tcp套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定ip和port    
    tcp_server_socket.bind(('',8080))    
    #使套接字被动链接
    tcp_server_socket.listen(128)
    while True:
        #等待链接
        print('等待...')
        client_socket,client_addr=tcp_server_socket.accept()
        print('等待...%s' % str(client_addr))
        while True:
            #发送接收数据_服务器一般先收后发
            recv_data=client_socket.recv(1024)
            if recv_data:
                print(recv_data.decode('utf-8'))
                client_socket.send('hello'.encode('utf-8'))
            else:
                break
        #关闭套接字
        client_socket.close()
    tcp_server_socket.close()


if __name__=='__main__':
    main()

