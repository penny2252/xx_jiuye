import socket
def main():
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #获取对方的IP和port
    dest_ip=input('请输入对方的ip:')
    dest_port=int(input('请输入对方的port:'))
    #绑定ip和port
    local_addr=('',8081)
    udp_socket.bind(local_addr)
    while True:
        #从键盘获取数据
        send_data=input('请输入想要发送的信息:')
        #使用套接字发送数据
        udp_socket.sendto(send_data.encode('utf-8'),(dest_ip,dest_port))
        #接收数据
        recev_data=udp_socket.recvfrom(1024)
        recev_ip=recev_data[1]
        recev_msg=recev_data[0]
        print('%s:%s'%(recev_ip,recev_msg.decode('gbk')))
    #关闭套接字
    udp_socket.close()

if __name__=='__main__':
    main()
	
