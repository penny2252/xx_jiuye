import socket
def main():
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    local_addr=('192.168.31.231',8081)
    udp_socket.bind(local_addr)
    #接受打印数据
    while True:
        recv_data=udp_socket.recvfrom(1024)
        #发送方的ip
        remot_addr=recv_data[1]
        #接收的信息
        recv_msg=recv_data[0]
        print('%s:%s'%(str(remot_addr),recv_msg.decode('gbk')))    
    #关闭套接字
    udp_socket.close()

if __name__=='__main__':
    main()
	
