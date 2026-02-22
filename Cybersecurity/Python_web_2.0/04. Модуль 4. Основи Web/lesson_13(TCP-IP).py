"""
    # Cтек протоколів TCP/IP
Відповідно до способів взаємодії мережею, програми можна поділити на дві категорії:
*без встановлення з'єднання (протокол UDP)
*із встановленням з'єднання (протокол TCP)
"""
#====================================================================================================
    # ! Ехо-сервер: UDP протокол !
#====================================================================================================
    # Код сервера:
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Received data: {data.decode()} from: {address}')
            sock.sendto(data, address)
            print(f'Send data: {data.decode()} to: {address}')

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    run_server(UDP_IP, UDP_PORT)
"""
Received data: Python from: ('127.0.0.1', 57422)
Send data: Python to: ('127.0.0.1', 57422)
Received data: Web from: ('127.0.0.1', 57422)
Send data: Web to: ('127.0.0.1', 57422)
Received data: development from: ('127.0.0.1', 57422)
Send data: development to: ('127.0.0.1', 57422)
"""
#====================================================================================================
    # Код клієнта:
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    for line in MESSAGE.split(' '):
        data = line.encode()
        sock.sendto(data, server)
        print(f'Send data: {data.decode()} to server: {server}')
        response, address = sock.recvfrom(1024)
        print(f'Response data: {response.decode()} from address: {address}')
    sock.close()


if __name__ == '__main__':
    run_client(UDP_IP, UDP_PORT)
"""
Send data: Python to server: ('127.0.0.1', 8080)
Response data: Python from address: ('127.0.0.1', 8080)
Send data: Web to server: ('127.0.0.1', 8080)
Response data: Web from address: ('127.0.0.1', 8080)
Send data: development to server: ('127.0.0.1', 8080)
Response data: development from address: ('127.0.0.1', 8080)
"""
#====================================================================================================
    # ! Ехо-сервер: TCP протокол !
#====================================================================================================
    #Код сервера:
import socket
from concurrent import futures as cf

TCP_IP = 'localhost'
TCP_PORT = 8080


def run_server(ip, port):
    def handle(sock: socket.socket, address: str):
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024)
            if not received:
                break
            data = received.decode()
            print(f'Data received: {data}')
            sock.send(received)
        print(f'Socket connection closed {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print(f'Start echo server {server_socket.getsockname()}')
    with cf.ThreadPoolExecutor(10) as client_pool:
        try:
            while True:
                new_sock, address = server_socket.accept()
                client_pool.submit(handle, new_sock, address)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()


if __name__ == '__main__':
    run_server(TCP_IP, TCP_PORT)

#====================================================================================================
    #Код клієнта:
import socket

TCP_IP = 'localhost'
TCP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        for line in MESSAGE.split(' '):
            print(f'Send data: {line}')
            sock.send(line.encode())
            response = sock.recv(1024)
            print(f'Response data: {response.decode()}')
    print(f'Data transfer completed')


if __name__ == '__main__':
    run_client(TCP_IP, TCP_PORT)

#====================================================================================================
