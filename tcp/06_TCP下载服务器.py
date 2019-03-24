import socket
def send(client_addr,client_socket):
    #5接受请求
    file_name=client_socket.recv(1024).decode('utf-8')
    #6发送文件
    txt=None
    try:
        f=open(file_name,'rb')
        txt=f.read()
        f.close()
    except Exception as ret:
        print('   ')
    if txt:
        client_socket.send(txt)

def main():
    #1创建套接字    
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2绑定ipport
    tcp_server_socket.bind(('',8080))
    #3listen
    tcp_server_socket.listen(128)
    #4acept
    while True:
        client_socket,client_addr=tcp_server_socket.accept()
        send(client_addr,client_socket)
    #8关闭套接字
        client_socket.close()
    tcp_server_socket.close()




if __name__=='__main__':
    main()
