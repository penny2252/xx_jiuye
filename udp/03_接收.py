import socket
def main():
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    local_addr=('192.168.31.231',8081)
    udp_socket.bind(local_addr)
    #接受打印数据
    recv_data=udp_socket.recvfrom(1024)
    print(recv_data)    
    #关闭套接字
    udp_socket.close()

if __name__=='__main__':
    main()
	
