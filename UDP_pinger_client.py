import socket
import datetime 
import statistics
import random

#服务器地址和端口
server_address=('127.0.0.1',12345)

#请求
request=b'Ping'

def main():
    i=10
    while i>0:
        #创建连接套接字
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #设置超时时间
        sock.settimeout(1)
        try:
            #开始发送请求的时间
            begin_time=datetime.datetime.now()
            sock.sendto(request,(server_address))
            #接收消息并处理
            while True:
                data,address=sock.recvfrom(2048)
                if data==b'Pong':
                    #接收到消息的时间
                    end_time=datetime.datetime.now()
                    i=i-1
                    break
                else:
                    #如果不是'Pong'，打印消息
                    print(data)
                    continue
        except socket.timeout:
            i-=1
            print('Request timed out')
        else: 
            #计算RTT
            sec=(end_time-begin_time).seconds
            print(f'RTT{11-i}:%f sec'%sec)

if __name__=='__main__':
    main()