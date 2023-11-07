import socket
import os

# 服务器地址和端口
server_address = ('127.0.0.1', 12345)

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1) 

print("FTP server is listening....")

while True:
    # 等待客户端连接
    client_socket, client_address = server_socket.accept()

    # 接收客户端发送的文件名
    file_name = client_socket.recv(1024).decode()

    if os.path.exists(file_name):
        # 如果文件存在，发送文件给客户端
        with open(file_name, 'rb') as f:
            data = f.read(1024)
            while data:
                client_socket.send(data)
                data = f.read(1024)
        print(f"'{file_name}' has been sent to the client")
    else:
        # 如果文件不存在，发送错误消息给客户端
        error_message = "not found"
        client_socket.send(error_message.encode())
        print(f"send error message to the client：'{error_message}'")

    # 关闭客户端套接字
    client_socket.close()
