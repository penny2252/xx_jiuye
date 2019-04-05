import socket
def main():
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #使用套接字发送数据
    udp_socket.sendto(b'haha',('192.168.31.120',8080))    
    #关闭套接字
    udp_socket.close()

if __name__=='__main__':
	main()
	
