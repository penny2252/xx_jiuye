import socket


def server(new_socket):
    new_socket.recv(1024)
    data='HTTP/1.1 200 OK\r\n'
    data+='\r\n'
    data+='<h1>hello</h1>'
    new_socket.send(data.encode('utf-8'))
    new_socket.close()


def main():
    tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.bind(('',8901))
    tcp_server.listen(128)
    while True:
        new_socket,new_addr=tcp_server.accept()
        server(new_socket)
    tcp_server.close()




if __name__=='__main__':
    main()
