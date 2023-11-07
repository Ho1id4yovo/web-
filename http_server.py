import socket
import os 

#读取文件
def read_file(file_path):
    if not os.path.exits(file_path):
        return None
    with open(file_path,'rb') as f:
        content=f.read()
    return content

#读取和解析来自用户端的传入请求
def iter_lines(sock:socket.socket,bufsize:int=16_384):
    """尽可能多地从bufsize块中读取数据，将数据连接在一个缓冲区(buff)中并不断将缓冲区分成单独的行
    一旦找到空行，返回它读取的额外数据"""
    buff=''
    while True:
        data=sock.recv(bufsize)
        if not data:
            return ''
        
        buff+=data
        while True:
            try:
                i=buff.index('\r\n')
                line,buff=buff[:i],buff[i+2:]
                if not line:
                    return buff
                yield line
            except IndexError:
                break

def main():
    #创建服务器套接字
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定服务器ip地址和端口
    server.bind('127.0.0.1',8080)

    #监听客户端连接
    server.listen(5)

    #接收客户端连接并处理请求
    while True:
        client_socket,client_address=server.accept()
        #从客户端接收HTTP请求
        request_data=client_socket.recv(1024).decode('utf-8')
        #解析请求行
        request_lines=request_data.split('\r\n')
        request_line=request_lines[0]
        method,url,http_version=request_line.aplit(' ')
        with client_socket:
            for request_line in iter_lines(client_socket):
                print(line)

        file_path='www'+url
        file_content=read_file(file_path)

        #根据文件内容构建HTTP响应
        if file_content:
            response_line='HTTP/1.1 200 OK\r\n'
            response_body=file_content
        else:
            response_line='HTTP/1.1 404 Not Found\r\n'
            response_body='<h2>404 Not Found</h2>'
        
        client_socket.send(response_line.encode('utf-8'))
        client_socket.send('Content-Type: text/html\r\n')
        client_socket.send('\r\n')
        client_socket.send(response_body)
        client_socket.close()

if '__name__'=='__main__':
    main()
