"""
    # !Сокет (Socket) !
це програмний інтерфейс для забезпечення інформаційного обміну між процесами. 
Існують клієнтські та серверні сокети. 
Серверний сокет прослуховує певний порт, а клієнтський підключається до сервера.
Python дозволяє виконувати передачу повідомлень між застосунками на нижчому рівні — за допомогою протоколу TCP/IP
"""
#====================================================================================================
import socket


sock = socket.socket()

#====================================================================================================
    #! Серверна частина !
#====================================================================================================
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
conn.close()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#====================================================================================================
import socket


def echo_server(host, port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                print(f'From client: {data}')
                if not data:
                    break
                conn.send(data.upper())

#====================================================================================================
    #! Клієнтська частина !
#====================================================================================================
from time import sleep

def simple_client(host, port):
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, port))
                s.sendall(b'Hello, world')
                data = s.recv(1024)
                print(f'From server: {data}')
                break
            except ConnectionRefusedError:
                sleep(0.5)

#====================================================================================================
import threading


HOST = '127.0.0.1'
PORT = 55555

server = threading.Thread(target=echo_server, args=(HOST, PORT))
client = threading.Thread(target=simple_client, args=(HOST, PORT))

server.start()
client.start()
server.join()
client.join()
print('Done!')

"""
Connected by ('127.0.0.1', 46948)
From client: b'Hello, world'
From server: b'HELLO, WORLD'
From client: b''
Done!
"""
#====================================================================================================
