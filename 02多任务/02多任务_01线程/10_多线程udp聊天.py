import socket
import threading


def send(udp_socket,server_addr):
    while True:
        send_msg=input('')
        udp_socket.sendto(send_msg.encode('utf-8'),server_addr)

def recv(udp_socket):
    while True:
        recv_msg=udp_socket.recvfrom(1024)
        print('%s:%s'%recv_msg[1],recv_msg[0].decode('utf-8'))
def main():
    """完成udp聊天的整体控制"""
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    udp_socket.bind(('',8981))
    server_addr=('192.168.31.231',8080)
    
    t1=threading.Thread(target=send, args=(udp_socket,server_addr))
    t2=threading.Thread(target=recv, args=(udp_socket,))
    t1.start()
    t2.start()    
    udp_socket.close()
    

if __name__ == '__main__':

    main()
