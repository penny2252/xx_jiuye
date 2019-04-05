# coding=utf-8
# static web server 
import re 
import socket 
from multiprocessing import Process 
# 定义发送文件根目录 
HTML_ROOT_DIR = "./html" 
def main(): 
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcp_sock.bind(("", 7777)) 
    tcp_sock.listen(128) 
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    while True: 
        cli_sock, cli_addr = tcp_sock.accept() 
        print("[{0}] 用户已连接...".format(cli_addr)) 
        cli_process = Process(target=handle_cli, args=(cli_sock,)) 
        cli_process.start() # socket 传入线程后关闭? 不明白 
        cli_sock.close() 
def handle_cli(cli_sock): 
    """handle client requests""" 
    # 获取数据，decode为字符串 
    request_data = cli_sock.recv(1024).decode("utf-8") 
    # print("requested: ", request_data) 
    request_lines = request_data.splitlines() 
    for line in request_lines: 
        print("=======", line) 
        # 正则解析报文，提取请求文件名 "GET / HTTP/1.1" 
        # 下面在第二次网页连入时，IndexError: list index out of range 
        response_start_line = request_lines[0] 
        file_name = re.match(r"\w+\s+(/[^\s]*)\s", response_start_line).group(1) 
        # 设置主页默认文件 
        if file_name == "/": 
            file_name = "/simple_html.html" 
        try: 
            with open(HTML_ROOT_DIR + file_name, "rb") as file: 
                # 此处decode为字符串，否则浏览器收到数据为字节形式
                file_data = file.read().decode("utf-8") 
        except IOError as e: 
        # 构造失败响应数据,符合HTTP规范 
            response_start_line = "HTTP/1.1 404 not found\r\n" 
            response_headers = "Server: My server\r\n" 
            response_body = "file not found" 
        else: # 构造成功响应数据,符合HTTP规范 
            response_start_line = "HTTP/1.1 200 OK\r\n" 
            response_headers = "Server: My server\r\n" 
            response_body = file_data 
        response = response_start_line + response_headers + "\r\n" + response_body 
        print("response: ", response) 
        # 发送响应数据 
        cli_sock.send(response.encode("utf-8")) 
        # 发送后关闭客户端 
        cli_sock.close() 
if __name__ == '__main__': 
    main()
