import socket

def main():
    #1创建套接字    
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2获取服务器ipport
    dest_ip=input('请输入ip')
    dest_port=int(input('请输入port'))
    #3 链接服务器
    tcp_socket.connect((dest_ip,dest_port))
    #4获取下载的文件名字
    file_name=input('请输入文件名')
    #5将文件名字发送到服务器
    tcp_socket.send(file_name.encode('utf-8'))
    #6接受文件的数据
    recv_data=tcp_socket.recv(1024)
    #7保存接受的数据
    if recv_data:
        with open('[xin]'+file_name,'wb') as f:
            f.write(recv_data) 
    #8关闭套接字
    tcp_socket.close()




if __name__=='__main__':
    main()
