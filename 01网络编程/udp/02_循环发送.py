import socket
def main():
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    udp_socket.bind(("",8080)) 
    
    #使用套接字发送数据
    while True:
        send_msg=input('输入发送的信息：')
        if send_msg=='exit':
            break
        udp_socket.sendto(send_msg.encode('utf-8'),('192.168.31.120',8080))    
    #关闭套接字
    udp_socket.close()

if __name__=='__main__':
    main()
	
