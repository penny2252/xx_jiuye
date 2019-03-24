import socket

def send_msg(udp_socket):
    desk_addr=('192.168.31.120',8080)
    send_data=input('请输入发送信息：')
    udp_socket.sendto(send_data.encode('utf-8'),desk_addr)
def recv_msg(udp_socket):
    recv_data=udp_socket.recvfrom(1024)
    print('%s:%s'%(recv_data[1],recv_data[0].decode('gbk')))
def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(('',8081))
    while True:
        print('1、发送，2、接收，3、退出')
        op=input('请选择操作')
        if op =='1':
            send_msg(udp_socket)
        elif op=='2':
            recv_msg(udp_socket)
        else:
            break

if __name__=='__main__':
    main()
