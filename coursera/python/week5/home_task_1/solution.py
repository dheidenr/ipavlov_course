import time
import socket


class Client:

    def __init__(self, address, port, timeout):
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.bind((address, port))
        # self.sock.listen(socket.SOMAXCONN)
        self.sock = socket.create_connection((address, port), timeout)
        self.conn, self.addr = self.sock.accept()
        self.conn.settimeout(timeout)

        self.key = address
        self.value = port
        self.timeout = timeout
        # timestamp = timestamp or int(time.time())

    def get(self, key):
        data = self.conn.recv(1000000)
        print(data)
        return print(f'{key}\n')

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        print(f'put {key} {value} {timestamp}\n')

    def __str__(self):
        return f'sock: {self.sock}, conn:{self.conn}, addr:{self.addr}, timeout: {self.timeout}'

