import socket
import threading

def send(tcp_socket):
    while True:
        send_data=input('请输入信息')
        tcp_socket.send(send_data.encode('utf-8'))

def recv(tcp_socket):
    while True:
        recv_data=tcp_socket.recvfrom(1024)
        print(recv_data)



def main():
    #创建tcp套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #tcp_socket.bind(('',8080))    
    #链接服务器
    #server_ip=input('请输入服务器ip：')
    #server_port=int(input('请输入服务器的端口：'))
    server_addr=('192.168.31.231',8080)
    tcp_socket.connect(server_addr)
    t1 = threading.Thread(target=send,args=(tcp_socket,))
    t2 = threading.Thread(target=recv,args=(tcp_socket,))
    t1.start()
    t2.start()
    #关闭套接字
    tcp_socket.close()


if __name__=='__main__':
    main()

