import socket


def main():
    #创建tcp套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #tcp_socket.bind(('',8080))    
    #链接服务器
    #server_ip=input('请输入服务器ip：')
    #server_port=int(input('请输入服务器的端口：'))
    server_addr=('192.168.31.231',8080)
    tcp_socket.connect(server_addr)
    #发送接收数据
    while True:
        send_data=input('请输入信息')
        if send_data=='exit':
            break
        tcp_socket.send(send_data.encode('utf-8'))
        recv_data=tcp_socket.recvfrom(1024)
        #print('%s:%s'%(recv_data[1],recv_data[0].decode('gbk')))
        print(recv_data)
    #关闭套接字
    tcp_socket.close()


if __name__=='__main__':
    main()

