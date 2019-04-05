import socket
import time            
#创建套接字
tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket关闭后系统马上释放端口
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#绑定服务器信息
tcp_server_socket.bind(('',7890))
#监听
tcp_server_socket.listen(128)
tcp_server_socket.setblocking(False)#设置套接字非堵塞
client_socket_list=list()
while True:
    time.sleep(0.5)
    #等待接入
    try:
        new_socket,client_addr=tcp_server_socket.accept()
    except Exception as ret:
        print('没有客户端接入,当前客户数量%d，列表：%s'%(len(client_socket_list),client_socket_list))
    else:
        client_socket_list.append(new_socket)
        new_socket.setblocking(False)
        #接收
    for client_socket in client_socket_list:
        try:
            recv_data=client_socket.recv(1024)
        except Exception as ret:
            print('没有收到客户端数据')
        else:
            print('数据：%s'%recv_data.decode('utf-8'))
            if recv_data:
                print('接收数据')
            else:
                client_socket_list.remove(client_socket)
                client_socket.close()
                print('客户端关闭')

