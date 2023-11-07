import socket 
import random
import time 

#服务器地址
server_address=('127.0.0.1',12345)

def server():
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((server_address))
    print('Serving on port 12345')
    
    while True:
        request,address=sock.recvfrom(2048)
        response='Wrong CMD'
        
        if random.random() < 0.3:
            print(f"Packet from {address} dropped")
            continue
        
        # 模拟随机延迟
        time.sleep(random.uniform(0.1, 0.5))
    
        
        #若请求为'Ping'，则响应'Pong'
        if request==b'Ping':
            response=b'Pong'
            sock.sendto(response,address)
        
if __name__=='__main__':
    server()