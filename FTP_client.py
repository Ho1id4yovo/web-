import socket

# 服务器地址和端口
server_address = ('127.0.0.1', 12345)

# 创建TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect(server_address)

# 输入要请求的文件名
file_name = input("please input the flie name you want to request: ")

# 发送文件名到服务器
client_socket.send(file_name.encode())

# 接收服务器的响应
response = client_socket.recv(1024).decode()

if response == "not found":
    print("the error message has been reveived：not found")
else:
    # 如果没有错误，保存接收到的文件
    with open(file_name, 'wb') as f:
        f.write(response.encode())
        print(f"receive the file: '{file_name}'")

# 关闭客户端套接字
client_socket.close()
